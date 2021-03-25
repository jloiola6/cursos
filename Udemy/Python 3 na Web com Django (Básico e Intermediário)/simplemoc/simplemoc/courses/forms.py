from django import forms


class CourseContact(forms.Form):

    name = forms.CharField(label= 'Nome', max_length= 100)
    email = forms.EmailField(label= 'E-mail')
    message = forms.CharField(label= 'Mensagem/Dúvida', widget= forms.Textarea)

# from django.forms import ModelForm
# from .models import Course

# class ContactCourse(ModelForm):
#     def __init__(self, *args, **kwargs):
#         for f in self.base_fields:
#             self.base_fields[f].widget.attrs['class'] = 'form-control'
#             self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
#             self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
#             self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
#         super(Form_Register, self).__init__(*args, **kwargs)

#     class Meta():
#         model = Course
#         fields = '__all__'


