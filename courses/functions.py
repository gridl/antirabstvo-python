from . import models


def new_access_to_course(user, course):
    course_sections = models.CourseSection.objects.filter(course_id=course)
    access = models.UserAccessToCourse(
        user=user,
        course=course,
        progress_section=course_sections.first()
    )
    access.save()


def have_access_to_course(user, course):
    access = models.UserAccessToCourse.objects.filter(
        user=user,
        course=course
    ) or None
    return access
