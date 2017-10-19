# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from alibot.guardian.models import Guardian


class Kid(models.Model):
    full_name = models.CharField(_('full name'), max_length=50)
    age = models.SmallIntegerField(_('age'), blank=True, null=True)
    guardian = models.ForeignKey(Guardian, related_name='kids', null=True, blank=True)

    class Meta:
        verbose_name = _('Kid')
        verbose_name_plural = _('Kids')

    def __unicode__(self):
        return '%s' % self.full_name


class Report(models.Model):
    TYPE_ABSENCE = 'A'
    TYPE_REQUEST = 'R'
    TYPE_CHOICES = (
        (TYPE_ABSENCE, _('absence')),
        (TYPE_REQUEST, _('request'))
    )

    report_type = models.CharField(_('Report type'), max_length=1, choices=TYPE_CHOICES)
    kid = models.ForeignKey(Kid, related_name='reports')
    reporter = models.ForeignKey(Guardian, related_name='reports')
    description = models.TextField(_('Description'))
    response = models.TextField(_('Response'))
    response_sent = models.BooleanField(editable=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
