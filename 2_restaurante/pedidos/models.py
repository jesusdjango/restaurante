from django.db import models
from ckeditor.fields import RichTextField
from plates.models import Plate

# Create your models here.
class Pedido(models.Model):


   #key = models.SlugField(verbose_name="Clave Plato", max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name="Nombre del cliente") 
    estado = models.CharField(max_length=10, verbose_name="Estado del pedido") 
    platos = models.ManyToManyField(Plate, verbose_name="Platos", related_name="get_posts")  # Enlazamos con la otra tabla 
    total = models.DecimalField(verbose_name="Total Precio", max_digits=6, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")       

    class Meta:
        verbose_name = "pedido"    
        verbose_name_plural = "pedidos"   
        ordering = ["-created"]    
        
    def __str__(self):
        return self.name     