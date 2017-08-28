# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from alibot.kid.models import Kid, Report


class ReportInlineAdmin(admin.TabularInline):
    model = Report
    extra = 0
    readonly_fields = ('reporter', 'created_at', 'description', 'report_type')
    can_delete = False


class KidAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'age', 'guardian')
    inlines = (ReportInlineAdmin,)


class ReportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Kid, KidAdmin)
admin.site.register(Report, ReportAdmin)
