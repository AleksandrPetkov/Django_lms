"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from groups.views import get_groups, create_group_view, update_group, detail_group
from students.views import create_student_view, get_students, index, update_student, detail_student
from teachers.views import get_teachers, update_teacher, detail_teacher, create_teacher_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student_view),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('groups/', get_groups),
    path('groups/create/', create_group_view),
    path('groups/update/<int:pk>/', update_group),
    path('groups/detail/<int:pk>/', detail_group),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher_view),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/detail/<int:pk>/', detail_teacher)
]
