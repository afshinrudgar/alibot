# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from alibot.guardian.validators import MobileNumberValidator
from .managers import GuardianManager


class Guardian(AbstractBaseUser):
    mobile_number = models.CharField(
        _('Mobile number'), max_length=11, validators=[MobileNumberValidator()]
    )
    telegram_username = models.CharField(
        _('Telegram username'), max_length=50, null=True, blank=True
    )
    telegram_id = models.CharField(
        _('Telegram id'), max_length=50, null=True, blank=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    password = None

    objects = GuardianManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['mobile_number', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('guardian')
        verbose_name_plural = _('guardians')
        unique_together = ('first_name', 'last_name')

    def is_logged_in(self):
        return self.telegram_id is not None

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
