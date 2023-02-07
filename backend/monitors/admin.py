from django.contrib import admin

from .models import Monitor, MonitorStatus


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = (
        'monitor_type',
        'friendly_name',
        'url_or_ip',
        'monitoring_interval',
        'monitor_ssl',
        'port'
    )

    list_filter = (
        'friendly_name',
        'url_or_ip'
    )


@admin.register(MonitorStatus)
class MonitorStatusAdmin(admin.ModelAdmin):
    list_display = (
        'monitor',
        'url_ip_up',
        'ssl_up',
        'date_timer'
    )

    list_filter = (
        'monitor',
    )
