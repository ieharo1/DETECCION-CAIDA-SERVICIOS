from django.contrib import admin
from .models import Service, CheckLog, NotificationSetting


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'endpoint', 'is_active', 'last_status', 'last_checked_at')
    list_filter = ('service_type', 'is_active', 'last_status')
    search_fields = ('name', 'endpoint')


@admin.register(CheckLog)
class CheckLogAdmin(admin.ModelAdmin):
    list_display = ('service', 'checked_at', 'is_up', 'status_code', 'response_time_ms')
    list_filter = ('is_up', 'service')
    search_fields = ('service__name', 'error_message')


@admin.register(NotificationSetting)
class NotificationSettingAdmin(admin.ModelAdmin):
    pass
