from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    template_name =  'courses/index.html'

    courses = Courses.objects.all()
    return TemplateResponse(request, template_name, locals())

def details(request, slug):
    template_name =  'courses/details.html'

    course = get_object_or_404(Courses, slug= slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            valido = True
            form.send_email(course)
            # print(form.cleaned_data['name'])
            form = ContactCourse()

    else:
        form = ContactCourse()

    return TemplateResponse(request, template_name, locals())
