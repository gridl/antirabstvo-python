from django.contrib import admin
from . import models


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_created', 'status')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creator', None) is None:
            obj.creator = request.user
        obj.save()


admin.site.register(models.News, NewsAdmin)
