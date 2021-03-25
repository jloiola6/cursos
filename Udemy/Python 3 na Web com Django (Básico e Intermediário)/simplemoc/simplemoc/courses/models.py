from django.db import models

# Create your models here.

class CourseManager(models.Model):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains= query) | models.Q(description__icontains= query))


class Course(models.Model):

    name = models.CharField('Nome', max_length= 100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descricao')
    start_date = models.DateField('Data de Inicio', null= True, blank= True)
    image = models.ImageField(upload_to= 'courses/images', verbose_name= 'Imagens', null= True, blank= True)

    created_at = models.DateField('Criado em', auto_now_add= True)
    update_at = models.DateField('Atualizado em', auto_now= True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
    
