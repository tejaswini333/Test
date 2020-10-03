from django.contrib import admin
from django.urls import path,include

# will hold -- application urls --

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('studreg.urls')),
    path('courses/', include('courseapp.urls')),
]
