from django.db import models
from django.contrib.auth.models import User

monitor_choices = [
    ['Ping', 'Ping'],
    ['HTTP(S)', 'HTTP(S)'],
    ['Port', 'Port']
]


class Monitor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    monitor_type = models.CharField(max_length=100, choices=monitor_choices)

    friendly_name = models.CharField(max_length=100)

    url_or_ip = models.CharField(max_length=100)

    monitoring_interval = models.IntegerField()

    monitor_timeout = models.IntegerField(default=30)

    monitor_ssl = models.BooleanField(default=False)

    port = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.friendly_name


class MonitorStatus(models.Model):

    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)

    url_ip_up = models.BooleanField(default=False)

    ssl_up = models.BooleanField(default=False)

    date_timer = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.monitor.friendly_name
