# Generated by Django 4.1.6 on 2023-02-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_type', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(max_length=100)),
                ('url_or_ip', models.CharField(max_length=100)),
                ('monitoring_interval', models.IntegerField()),
                ('monitor_ssl', models.BooleanField(default=False)),
            ],
        ),
    ]