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



from django.urls import path

from courses.views import get_courses
from courses.views import create_course_view
from courses.views import update_course
from courses.views import detail_course
from courses.views import delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course_view, name='create'),
    path('update/<int:pk>/', update_course, name='update'),
    path('detail/<int:pk>/', detail_course, name='detail'),
    path('delete/<int:pk>/', delete_course, name='delete'),

]
