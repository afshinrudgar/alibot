# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guardian', '0006_auto_20170827_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, verbose_name='code')),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guardian.Guardian', verbose_name='guardian')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramIdStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(verbose_name='Telegram id')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guardian.Guardian', verbose_name='guardian')),
            ],
        ),
    ]