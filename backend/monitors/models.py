from django.db import models


class Monitor(models.Model):
    monitor_type = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    url_or_ip = models.CharField(max_length=100)
    monitoring_interval = models.IntegerField()
    monitor_ssl = models.BooleanField(default=False)

    def __str__(self):
        return self.friendly_name
