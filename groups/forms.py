from django import forms
from django_filters import FilterSet

from groups.models import Group
from students.models import Student


class GroupBaseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), required=False)

    def save(self, commit=True):
        new_group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()


    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start',
            'group_description'
        ]
        widgets = {
            'group_start': forms.DateInput(attrs={'type': 'date'})
        }


class CreateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True)

    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all()

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start'
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains']
        }
