from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import models

@login_required
def my_courses(request):
    current_user_courses = models.UserAccessToCourse.objects.filter(user=request.user)
    context = {'my_courses': current_user_courses}
    return render(request, 'courses/my.html', context)


@login_required
def course_page(request, pk):
    current_user_progress = models.UserAccessToCourse.objects.filter(
        user=request.user,
        course=pk
    ).first()
    if not current_user_progress:
        raise PermissionDenied
    course_sections = models.CourseSection.objects.filter(course_id=pk)
    context = {
        'sections': course_sections,
        'progress': current_user_progress
    }
    return render(request, 'courses/course.html', context)


@login_required
def section_page(request, pk):
    section = get_object_or_404(models.CourseSection, pk=pk)
    user_access = models.UserAccessToCourse.objects.filter(
        user=request.user,
        course=section.course_id
    ).first()
    if not user_access or user_access.progress_section.pk < int(pk):
        raise PermissionDenied
    try:
        homework = models.Homework.objects.get(section_id=section)
    except models.Homework.DoesNotExist:
        homework = None
    user_homework = None
    if homework is not None:
        try:
            user_homework = models.UserHomework.objects.get(
                user=request.user,
                homework=homework)
        except models.UserHomework.DoesNotExist:
            user_homework = None
    context = {
        'section': section,
        'homework': homework,
        'user_homework': user_homework
    }
    return render(request, 'courses/section.html', context)


def next_section(request, pk):
    section = get_object_or_404(models.CourseSection, pk=pk)
    user_access = models.UserAccessToCourse.objects.filter(
        user=request.user,
        course=section.course_id
    ).first()
    course_sections = models.CourseSection.objects.filter(
        course_id=section.course_id,
        pk__gt=pk
    )
    user_access.progress_section = course_sections.first()
    user_access.save()
    return HttpResponseRedirect(reverse('courses:section_detail', kwargs={'pk': course_sections.first().pk}))
