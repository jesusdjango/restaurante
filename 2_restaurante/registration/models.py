from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #Esto es para poder decorar la señal (un decorador de django)
from django.db.models.signals import post_save #Esta es un tipo de señal, como digo abajo (después de grabar) hay para antes de grabar, después de borrar, antes de borrar... etc...

# Vamos a crear una función para borrar la foto del avatar antigua y quedasrnos solo con la nueva, sino es un derroche de espacio en memoria gastado.
# la instance del parametro hace referencia a la instancia que se está guardando pero después de haber confirmado el nuevo valor. Y el filename, es el fichero ya con la imagen que vamos a sobreescribir
def custom_upload_to(instance, filename):
    #Obtenemos primero la vieja instancia con su primary key (pk)
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()   #Una vez que tenemos la instancia anterior, borramos el avatar.
    return "profiles/" + filename  #Y devolvemos ya el fichero con el avatar nuevo.
    # Y cambiamos en "upload_to" profiles por la función que acabamos de crear.


# Create your models here.
class Profile(models.Model):
    # Después de crear los 3 campos creamos el enlace con el usurio. Tiramos del modelo "User" que ya tenemos hecho.
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Relación uno a uno, y que borre en cascada, como ya dijimos, si borras el usurio, se borraria este reg de relación.

#   avatar = models.ImageField(upload_to="profiles", null=True, blank=True) # Este 1º campo es para la foto y null a true porque puede venir vacio.
    avatar = models.ImageField(upload_to= custom_upload_to, null=True, blank=True) # Cambiamos "profile" por la función de arriba que va a borrar el avatar viejo y solo se queda con el nuevo.
   
    bio = models.TextField(null=True, blank=True)   # Biografia, un testito
    link = models.URLField(max_length=200, null=True, blank=True)  # Enlace a páginas web

    #Para que ordene los perfiles por nombre de usuario, y que se nos quite el warning que nos salia de inconsistencia de datos.
    class Meta:
        ordering = ["user__username"]


#PARTE II 2, SEÑALES
#   Para poder llamarse a la señal, se tiene que auto llamar, para que se haga de manera automatica y
#y esto se hace decorandola. "receiver" tiene que ser así y  Con "post_save" le indicamos que se grabe después de crearse el usuario (después de grabar la instancia de usuario). Hay señales para indicar que se ejecute después de borrar una instancia, antes de borrarla, antes de grabar, después de grabarla, etc...  
@receiver(post_save, sender=User) #Le indicamos "User" que es el tipo de modelo que vamos a utilizar.
# Esto en si es una señal, creamos una instancia del objeto Profile (modelo que tenemos más arriba). Se va a llamar "ensure_profile_exists" por sentido común ya que se va a encargar de comprobar que el perfil existe. (asegurar_perfil_existe)
def ensure_profile_exists(sender, instance, **kwargs):
    # Si existe la clave "create", quiere decir que es la primera vez que se guarda esta instancia, entonces es cuando creamos el perfil. Y devolvemos "false" sino tiene esa entrada en el diccionario, para que la próxima vez ya no entre, solo la 1ª vez, que va a ser cuando encuentre el "create"
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")
