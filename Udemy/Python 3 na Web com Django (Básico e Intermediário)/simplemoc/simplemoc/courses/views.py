from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import CourseContact

# Create your views here.

def courses(request):
    template_name = 'courses/courses.html'

    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, template_name, context)


# def details(request, pk):
#     template_name = 'courses/details.html'
#     course = Course.objects.get(pk = pk)
#     context = {
#         'course': course
#     }

#     return render(request, template_name, context)


def details(request, slug):
    template_name = 'courses/details.html'
    course = get_object_or_404(Course, slug= slug)
    context = {}

    if request.method == 'POST':
        form = CourseContact(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            # print(form.cleaned_data['name']) #Vizualizar os dados do formulários
            form = CourseContact()

    else:
        form = CourseContact()

    context['course'] = course
    context['form'] = form

    return render(request, template_name, context)


