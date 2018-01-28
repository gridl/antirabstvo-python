from django.contrib import admin
from . import models


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_role')


class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id')


class UserAccessToCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress_section', 'date_start')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'progress_section', None) is None:
            course_sections = models.CourseSection.objects.filter(course_id=obj.course)
            obj.progress_section = course_sections.first()
        obj.save()


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.CourseSection, CourseSectionAdmin)
admin.site.register(models.Homework)
admin.site.register(models.UserAccessToCourse, UserAccessToCourseAdmin)
admin.site.register(models.UserHomework)

