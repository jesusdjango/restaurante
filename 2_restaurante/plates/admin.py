from django.contrib import admin
from .models import Plate

# Register your models here.
class PlateAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("name","price", "updated")
    list_filter = ('categories__name',)
    def post_categories(self, obj): 
        return ", ".join([c.name for c in obj.categories.all()])
    post_categories.short_description = "Categorías"

    # Inyectamos nuestro fichero css para el tamaño del movil
    class Media:
        css = {
            'all': ('plates/css/custom_ckeditor.css',)
        }
    
admin.site.register(Plate, PlateAdmin)

    



