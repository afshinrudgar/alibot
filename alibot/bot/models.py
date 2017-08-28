# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from alibot.guardian.models import Guardian


class CodeStore(models.Model):
    guardian = models.OneToOneField(Guardian, verbose_name=_('guardian'), unique=True, related_name='code_store')
    code = models.CharField(_('code'), max_length=4)
    last_update = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)


class TelegramIdStore(models.Model):
    id = models.PositiveIntegerField(_('Telegram id'), unique=True, primary_key=True)
    guardian = models.OneToOneField(Guardian, verbose_name=_('guardian'), unique=True, related_name='telegram')
    join_date = models.DateTimeField(auto_now_add=True)