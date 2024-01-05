from django.contrib import admin
from .models import Pedido

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("name","estado", "updated")
    list_filter = ('platos__name',)
    def post_platos(self, obj): 
        return ", ".join([c.name for c in obj.platos.all()])
    post_platos.short_description = "Platos"

    # Inyectamos nuestro fichero css para el tamaño del movil
    class Media:
        css = {
            'all': ('plates/css/custom_ckeditor.css',)
        }
    
admin.site.register(Pedido, PedidoAdmin)

    



