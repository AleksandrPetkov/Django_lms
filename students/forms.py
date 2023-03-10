from django import forms
from django_filters import FilterSet

from students.models import Student
from students.utils import normalize_phone


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'city',
            'phone'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        return normalize_phone(value)


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'city',
            'phone',
            'group'
        ]
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()

class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
