from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('courses/',courses, name='courses'),
    path('addcourses/',addcourses, name='addcourses'),
]
