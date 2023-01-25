from django import forms
from students.models import Student
from students.utils import normalize_phone


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'city',
            'phone'
        ]

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        return normalize_phone(value)
