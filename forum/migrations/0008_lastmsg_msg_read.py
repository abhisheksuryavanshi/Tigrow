# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_lastmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastmsg',
            name='msg_read',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
