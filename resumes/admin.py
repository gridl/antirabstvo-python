from django.contrib import admin
from . import models


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator', 'date_created', 'date_changed')


admin.site.register(models.Resume, ResumeAdmin)
