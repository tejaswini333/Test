from django.urls import path
from courseapp.views import *

#this file holds-- > courses related urls

#http://localhost:8000/courses/register/
#http://localhost:8000/courses/edit/
#http://localhost:8000/courses/delete/

urlpatterns = [
    path('register/', create_edit_new_course),
    path('edit/<int:crid>', fetch_course_info),
    path('delete/<int:crid>', delete_course_info),
]
