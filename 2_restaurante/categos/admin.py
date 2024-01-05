from django.contrib import admin
from .models import Category

# Register your models here.
class CategoAdmin(admin.ModelAdmin):  
    readonly_fields = ("created", "updated")

admin.site.register(Category, CategoAdmin) 

   



