# 🚨 Detección de Caídas de Servicios

<p align="center">
  <img src="https://img.icons8.com/color/200/000000/online-support.png" alt="Brutal Monitor Logo" width="200"/>
</p>

---

## 📱 Descripción

**Brutal Monitor** es un sistema de observabilidad en **Django + PostgreSQL** para vigilar URLs y APIs en tiempo real.

> El sistema ejecuta checks cada segundo (configurable por servicio), detecta caídas y recuperaciones, guarda historial para indicadores, y notifica por correo o Telegram.

---

## ✨ Características

### Funcionalidades Implementadas ✅

- ✅ **Monitoreo en Tiempo Real** - Check cada 1 segundo (o configurable)
- ✅ **Validación HTTP de URLs/APIs** - Método, timeout y status esperado
- ✅ **Registro Histórico Completo** - Logs de disponibilidad y latencia
- ✅ **Indicadores de Operación** - Online/Offline/Uptime/latencia promedio
- ✅ **Panel Responsive 100% Bootstrap 5** - Sin CSS custom
- ✅ **AJAX Liviano** - Actualización en vivo del dashboard
- ✅ **Notificaciones por Correo** - SMTP configurable
- ✅ **Notificaciones por Telegram** - Bot token + chat ID
- ✅ **Alertas por Caída y Recuperación**
- ✅ **CRUD de Servicios** - Agregar/editar servicios a monitorear
- ✅ **Panel de Administración Django** - Gestión avanzada
- ✅ **Docker Compose Completo** - Web + Worker + PostgreSQL

### Próximamente 🔄

- 📈 Gráficos de tendencia por servicio
- 🔐 OAuth2 / SSO para equipo DevOps
- 📬 Integración con Slack y Discord
- 🧠 Detección de degradación por anomalías
- 🌐 Múltiples nodos de monitoreo distribuidos

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Backend | Python | 3.12 |
| Framework | Django | 5.1.6 |
| DB | PostgreSQL | 16 |
| Frontend | Bootstrap | 5.3.3 |
| WSGI | Gunicorn | 23.0.0 |
| HTTP checks | requests | 2.32.3 |
| Orquestación | Docker Compose | v2+ |

---

## 📁 Estructura del Proyecto

```
brutal_monitor/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── monitor/
│   ├── management/commands/check_services.py
│   ├── migrations/0001_initial.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── notifications.py
├── templates/monitor/
│   ├── base.html
│   ├── dashboard.html
│   ├── service_list.html
│   ├── service_form.html
│   └── notification_form.html
├── static/js/dashboard.js
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── entrypoint.sh
└── README.md
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el Repositorio
```bash
git clone <TU_REPO>
cd Unity-desde0/brutal_monitor
```

### 2. Ejecutar con Docker Compose
```bash
# Construir y levantar servicios
docker compose up --build
```

### 3. Accesos
- App: `http://localhost:8000`
- Admin Django: `http://localhost:8000/admin`
- Usuario admin por defecto:
  - user: `admin`
  - pass: `admin123456`

### 4. Configurar notificaciones
1. Ir a **Configuración > Notificaciones**.
2. Activar correo y/o Telegram.
3. Guardar.



### 5. Generar ZIP local (sin versionar binarios)
```bash
cd ..
./brutal_monitor/scripts_create_zip.sh
```

Esto genera `brutal_monitor.zip` localmente para compartir/descargar, pero no se sube al repo.

---

## 📊 Modelo de Datos

### Servicio Monitoreado
```txt
name | Nombre del servicio
service_type | URL o API
endpoint | URL completa
method | GET/POST/etc.
expected_status | Código esperado (ej: 200)
timeout_seconds | Timeout por request
check_interval_seconds | Frecuencia de check
is_active | Activo/Inactivo
last_status | Último estado
last_response_time_ms | Última latencia
```

### Log de Monitoreo
```txt
service | Servicio asociado
checked_at | Fecha/hora del check
is_up | Disponible o caído
status_code | HTTP status recibido
response_time_ms | Latencia
error_message | Error capturado
```

---

## 🎯 Flujo de Monitoreo en Tiempo Real

```txt
1) Worker lee servicios activos
2) Evalúa si toca check según intervalo
3) Lanza request al endpoint
4) Compara status esperado
5) Guarda log (UP/DOWN)
6) Actualiza estado actual del servicio
7) Si cayó o se recuperó -> notifica por Email/Telegram
8) Dashboard refresca cada segundo por API interna
```

---

## 🔔 Variables para Email (SMTP)

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_password_app
EMAIL_USE_TLS=1
DEFAULT_FROM_EMAIL=alerts@tudominio.com
```

---

## 🤖 Telegram Bot

Necesitas:
1. `telegram_bot_token`
2. `telegram_chat_id`

Se configuran desde la interfaz del sistema.

---

## 👨‍💻 Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack Developer · Automatización · Data**

### 📞 Contacto

- 📧 **Email:** zackharo1@gmail.com
- 📱 **WhatsApp:** [+593 988055517](https://wa.me/593988055517)
- 💻 **GitHub:** [ieharo1](https://github.com/ieharo1)
- 🌐 **Portafolio:** [ieharo1.github.io](https://ieharo1.github.io/portafolio-isaac.haro/)

---

## 📄 Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

---

⭐ Si te gustó el proyecto, ¡dame una estrella en GitHub!
