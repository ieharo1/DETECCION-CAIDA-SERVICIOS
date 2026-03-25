from django.contrib import admin
from django.urls import path
from monitor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('servicios/', views.service_list, name='service_list'),
    path('servicios/nuevo/', views.service_create, name='service_create'),
    path('servicios/<int:pk>/editar/', views.service_update, name='service_update'),
    path('configuracion/notificaciones/', views.notification_settings_view, name='notification_settings'),
    path('api/resumen/', views.api_summary, name='api_summary'),
    path('api/logs/', views.api_logs, name='api_logs'),
]
