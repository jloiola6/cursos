from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='index'),
]