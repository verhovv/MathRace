# Generated by Django 5.1.3 on 2024-12-06 00:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_roomtask_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.car'),
        ),
    ]