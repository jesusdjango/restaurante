from django.db import models
# Create your models here.

class Category(models.Model):
    # key = models.SlugField(verbose_name="Clave Categoría", max_length=100, unique=True) 
    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)  
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)  
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)
     
    class Meta:
        verbose_name = "categoría"    
        verbose_name_plural = "categorías"   
        ordering = ["created"]    
        
    def __str__(self):
        return self.name      

  