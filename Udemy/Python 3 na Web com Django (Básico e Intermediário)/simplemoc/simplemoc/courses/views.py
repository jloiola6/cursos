from django.shortcuts import render
from .models import Course

# Create your views here.

def courses(request):
    template_name = 'courses/courses.html'

    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, template_name, context)
