# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170915_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='s',
            new_name='url',
        ),
    ]