




# ESTO LO ESTOY HACIENDO YO DE PRUEBA PARA VERLO EN EL ADMIN, PERO NO ESTÁ EN EL CURSO...
# QUERIA COMPROBAR QUE SI LO PONIA AQUI SE VEIA EN LA BBDD. Y SIIII...
from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', "link")  #faltaria bio, este es muy largo y no lo pongo, porque es lo que se va a ver antes de entrar al registro.

admin.site.register(Profile, ProfileAdmin)

# admin.site.register(Profile)     (también puedes hacer así la llamada y no te pone ningún campo al intentar verlo de primeras)
