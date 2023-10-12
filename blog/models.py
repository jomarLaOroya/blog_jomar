from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoría', max_length=100, null=False, blank=False)
    estado = models.BooleanField('Categoría Activada/No Activada', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres del autor', max_length=150, null=False, blank=False)
    apellidos = models.CharField('Apellidos del autor', max_length=250, null=False, blank=False)
    estado= models.BooleanField('Autor Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellidos,self.nombre)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=150, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripción', max_length=115, null=False, blank=False)
    contenido = RichTextField('Contenido')
    
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo
        
