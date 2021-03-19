from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<slug:slug>', views.details, name='details'),
]