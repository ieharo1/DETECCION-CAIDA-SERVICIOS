from django.contrib import messages
from django.db.models import Avg, Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ServiceForm, NotificationSettingForm
from .models import CheckLog, NotificationSetting, Service


def dashboard(request):
    services = Service.objects.filter(is_active=True)
    total = services.count()
    online = services.filter(last_status=True).count()
    offline = total - online
    uptime = round((online / total) * 100, 2) if total else 100

    last_logs = CheckLog.objects.select_related('service')[:20]
    avg_response = CheckLog.objects.aggregate(avg=Avg('response_time_ms'))['avg'] or 0

    context = {
        'total': total,
        'online': online,
        'offline': offline,
        'uptime': uptime,
        'avg_response': int(avg_response),
        'last_logs': last_logs,
        'services': services,
    }
    return render(request, 'monitor/dashboard.html', context)


def service_list(request):
    return render(request, 'monitor/service_list.html', {'services': Service.objects.all()})


def service_create(request):
    form = ServiceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Servicio creado correctamente.')
        return redirect('service_list')
    return render(request, 'monitor/service_form.html', {'form': form, 'title': 'Nuevo servicio'})


def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Servicio actualizado correctamente.')
        return redirect('service_list')
    return render(request, 'monitor/service_form.html', {'form': form, 'title': 'Editar servicio'})


def notification_settings_view(request):
    settings_obj, _ = NotificationSetting.objects.get_or_create(pk=1)
    form = NotificationSettingForm(request.POST or None, instance=settings_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Configuración guardada.')
        return redirect('notification_settings')
    return render(request, 'monitor/notification_form.html', {'form': form})


def api_summary(request):
    total = Service.objects.filter(is_active=True).count()
    online = Service.objects.filter(is_active=True, last_status=True).count()
    offline = total - online
    grouped = CheckLog.objects.values('service__name').annotate(
        total=Count('id'),
        fails=Count('id', filter=Q(is_up=False)),
    ).order_by('service__name')
    return JsonResponse({'total': total, 'online': online, 'offline': offline, 'indicators': list(grouped)})


def api_logs(request):
    logs = CheckLog.objects.select_related('service')[:50]
    data = [
        {
            'service': l.service.name,
            'is_up': l.is_up,
            'status_code': l.status_code,
            'response_time_ms': l.response_time_ms,
            'checked_at': l.checked_at.isoformat(),
            'error_message': l.error_message,
        }
        for l in logs
    ]
    return JsonResponse({'logs': data})
