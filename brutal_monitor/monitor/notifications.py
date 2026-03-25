import requests
from django.conf import settings
from django.core.mail import send_mail


def send_alert(notification, message):
    if not notification:
        return

    if notification.email_enabled and notification.email_to:
        recipients = [e.strip() for e in notification.email_to.split(',') if e.strip()]
        if recipients:
            send_mail(
                subject='🚨 Alerta Monitor de Servicios',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipients,
                fail_silently=True,
            )

    if notification.telegram_enabled and notification.telegram_bot_token and notification.telegram_chat_id:
        url = f"https://api.telegram.org/bot{notification.telegram_bot_token}/sendMessage"
        try:
            requests.post(url, json={"chat_id": notification.telegram_chat_id, "text": message}, timeout=5)
        except requests.RequestException:
            pass
