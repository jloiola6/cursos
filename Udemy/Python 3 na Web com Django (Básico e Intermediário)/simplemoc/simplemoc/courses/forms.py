from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemoc.core.mail import send_mail_template

class CourseContact(forms.Form):

    name = forms.CharField(label= 'Nome', max_length= 100)
    email = forms.EmailField(label= 'E-mail')
    message = forms.CharField(label= 'Mensagem/Dúvida', widget= forms.Textarea)

    def send_mail(self, course):
        print('Olá Mundo!')
        subject = f'[{course}] Contato'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )

    # def send_email(self, course):
    #     subject = f'[{course}] Contato'
    #     name = self.cleaned_data['name']
    #     email =  self.cleaned_data['email']
    #     message = self.cleaned_data['message']
    #     message = f'Nome: {name};\nE-mail: {email};\n\n {message}'

    #     send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=False) 




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


