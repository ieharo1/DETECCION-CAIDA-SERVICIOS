from django.db import models


class Service(models.Model):
    SERVICE_TYPES = (
        ('url', 'URL'),
        ('api', 'API'),
    )

    name = models.CharField(max_length=120)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES, default='url')
    endpoint = models.URLField(unique=True)
    method = models.CharField(max_length=10, default='GET')
    expected_status = models.PositiveSmallIntegerField(default=200)
    timeout_seconds = models.PositiveIntegerField(default=5)
    check_interval_seconds = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    last_checked_at = models.DateTimeField(null=True, blank=True)
    last_status = models.BooleanField(default=True)
    last_response_time_ms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CheckLog(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='logs')
    checked_at = models.DateTimeField(auto_now_add=True)
    is_up = models.BooleanField(default=False)
    status_code = models.IntegerField(null=True, blank=True)
    response_time_ms = models.PositiveIntegerField(default=0)
    error_message = models.TextField(blank=True)

    class Meta:
        ordering = ['-checked_at']


class NotificationSetting(models.Model):
    email_enabled = models.BooleanField(default=False)
    email_to = models.CharField(max_length=255, blank=True)
    telegram_enabled = models.BooleanField(default=False)
    telegram_bot_token = models.CharField(max_length=255, blank=True)
    telegram_chat_id = models.CharField(max_length=255, blank=True)
    notify_on_recovery = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Configuración de notificaciones'
