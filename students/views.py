from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
#from django.views.decorators.csrf import csrf_exempt
from webargs.fields import Str
from webargs.djangoparser import use_args
from django.db.models import Q
from django.urls import reverse

from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student
#from .utils import format_list_students


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query',
# )
def get_students(request):
    students = Student.objects.all().order_by('birthday')
    filter_form = StudentFilterForm(data=request.GET, queryset=students)
    return render(
        request=request,
        template_name='students/list.html',
        context={'filter_form': filter_form}
    )


def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'student': student})


def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/create.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/update.html', {'form':form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/delete.html', {'student': student})
