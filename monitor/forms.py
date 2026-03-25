from django import forms
from .models import Service, NotificationSetting


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name',
            'service_type',
            'endpoint',
            'method',
            'expected_status',
            'timeout_seconds',
            'check_interval_seconds',
            'is_active',
        ]


class NotificationSettingForm(forms.ModelForm):
    class Meta:
        model = NotificationSetting
        fields = [
            'email_enabled',
            'email_to',
            'telegram_enabled',
            'telegram_bot_token',
            'telegram_chat_id',
            'notify_on_recovery',
        ]
