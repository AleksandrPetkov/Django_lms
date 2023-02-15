from django import forms
from django_filters import FilterSet

from courses.models import Course


class CourseBaseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            'course_type',
            'lessons_number',
            'course_program'
        ]


class CreateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class UpdateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        pass


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_type': ['exact', 'icontains']
        }
