from django.urls import path
from studreg.views import *

#this file holds-- > student related urls

#http://localhost:8000/student/register/
#http://localhost:8000/student/edit/
#http://localhost:8000/student/delete/

urlpatterns = [
    path('register/', create_edit_new_student),
    path('edit/<int:sid>', fetch_student_info),
    path('delete/<int:sid>', delete_student_info)
]
