from django.contrib import admin
from django.urls import path
from . import views

#localhost:8000/all_app
urlpatterns = [
    path("", views.all_app,name='all_app'),
]
