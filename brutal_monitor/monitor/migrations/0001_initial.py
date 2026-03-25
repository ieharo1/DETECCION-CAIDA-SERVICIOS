from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_enabled', models.BooleanField(default=False)),
                ('email_to', models.CharField(blank=True, max_length=255)),
                ('telegram_enabled', models.BooleanField(default=False)),
                ('telegram_bot_token', models.CharField(blank=True, max_length=255)),
                ('telegram_chat_id', models.CharField(blank=True, max_length=255)),
                ('notify_on_recovery', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('service_type', models.CharField(choices=[('url', 'URL'), ('api', 'API')], default='url', max_length=10)),
                ('endpoint', models.URLField(unique=True)),
                ('method', models.CharField(default='GET', max_length=10)),
                ('expected_status', models.PositiveSmallIntegerField(default=200)),
                ('timeout_seconds', models.PositiveIntegerField(default=5)),
                ('check_interval_seconds', models.PositiveIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('last_checked_at', models.DateTimeField(blank=True, null=True)),
                ('last_status', models.BooleanField(default=True)),
                ('last_response_time_ms', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='CheckLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_at', models.DateTimeField(auto_now_add=True)),
                ('is_up', models.BooleanField(default=False)),
                ('status_code', models.IntegerField(blank=True, null=True)),
                ('response_time_ms', models.PositiveIntegerField(default=0)),
                ('error_message', models.TextField(blank=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='monitor.service')),
            ],
            options={'ordering': ['-checked_at']},
        ),
    ]
