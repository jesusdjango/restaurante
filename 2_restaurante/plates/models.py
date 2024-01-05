from django.db import models
from ckeditor.fields import RichTextField
from categos.models import Category

# Create your models here.
class Plate(models.Model):
   #key = models.SlugField(verbose_name="Clave Plato", max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name="Nombre del plato") 
    price = models.DecimalField(verbose_name="Precio", max_digits=5, decimal_places=2)
    categories = models.ManyToManyField(Category, verbose_name="Sus categorías", related_name="get_posts")  # Enlazamos con la otra tabla 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       

    class Meta:
        verbose_name = "plato"    
        verbose_name_plural = "platos"   
        ordering = ["created"]    
        
    def __str__(self):
        return self.name     