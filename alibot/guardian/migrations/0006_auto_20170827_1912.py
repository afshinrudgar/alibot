# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guardian', '0005_auto_20170827_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='last_login_code',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='last_login_code_request',
        ),
    ]