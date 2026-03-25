import time
import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from monitor.models import Service, CheckLog, NotificationSetting
from monitor.notifications import send_alert


class Command(BaseCommand):
    help = 'Monitorea servicios activos en tiempo real.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Worker de monitoreo iniciado...'))
        while True:
            now = timezone.now()
            settings_obj = NotificationSetting.objects.first()

            for service in Service.objects.filter(is_active=True):
                if service.last_checked_at:
                    elapsed = (now - service.last_checked_at).total_seconds()
                    if elapsed < service.check_interval_seconds:
                        continue

                is_up, status_code, response_ms, error_message = self.check_service(service)
                was_up = service.last_status

                CheckLog.objects.create(
                    service=service,
                    is_up=is_up,
                    status_code=status_code,
                    response_time_ms=response_ms,
                    error_message=error_message,
                )

                service.last_checked_at = now
                service.last_status = is_up
                service.last_response_time_ms = response_ms
                service.save(update_fields=['last_checked_at', 'last_status', 'last_response_time_ms'])

                if was_up and not is_up:
                    send_alert(settings_obj, f'❌ Caída detectada: {service.name} ({service.endpoint}) - {error_message or status_code}')
                elif not was_up and is_up and settings_obj and settings_obj.notify_on_recovery:
                    send_alert(settings_obj, f'✅ Recuperado: {service.name} ({service.endpoint})')

            time.sleep(1)

    def check_service(self, service):
        started = time.perf_counter()
        try:
            response = requests.request(service.method, service.endpoint, timeout=service.timeout_seconds)
            response_ms = int((time.perf_counter() - started) * 1000)
            is_up = response.status_code == service.expected_status
            err = '' if is_up else f'Status inesperado {response.status_code}'
            return is_up, response.status_code, response_ms, err
        except requests.RequestException as ex:
            response_ms = int((time.perf_counter() - started) * 1000)
            return False, None, response_ms, str(ex)
