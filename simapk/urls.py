from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("courses", views.courses, name="courses"),
    path("about", views.about, name="about"),
    path("details", views.details, name="details"),
]