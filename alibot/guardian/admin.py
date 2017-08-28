# -*- coding: utf-8 -*-
# !/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from alibot.guardian.models import Guardian
from alibot.kid.models import Kid


class KidsInlineAdmin(admin.TabularInline):
    model = Kid
    extra = 0


class GuardianAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('mobile_number',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    )
    inlines = (KidsInlineAdmin,)


admin.site.register(Guardian, GuardianAdmin)
