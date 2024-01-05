from django.db import models
from .forms import MiFormularioEmail, ProfileForm, EmailForm  #Sino que vamos a heredar de este formulario que hemos creado nosotros.
from django.forms.models import BaseModelForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms   #para acceder a los tipos de "widgets"
# from django.views.generic.base import TemplateView    # Para la clase del "Profile", pero lo cambiamos para el "UpdateView"
from django.views.generic.edit import UpdateView
from .models import Profile

from django.utils.decorators import method_decorator   # Esto para decorar la clase "profile"
from django.contrib.auth.decorators import login_required

# Create your views here. (vamos a crear la vista de registro basada en clase)
class SignUpView(CreateView):
#   form_class = UserCreationForm  #Vamos asignar el formulario ya creado "UserCreatioForm" (hecho por django) a la variable que vamos a utilizar
    # le cambiamos el formulario y le pasamos el que hemos hecho en el archivo "forms.py"
    form_class = MiFormularioEmail

    template_name = "registration/signup.html"

#   success_url = reverse_lazy("login") #Esto es para redireccionar a "login" justo después del registro.
    # "success_url" Ahora queremos devolver un sms a la página de "login" para decir que el usuario se ha registrado correctamente, no podemos hacerlo en la variable de arriba "success_url"
    #y lo que hacemos es redefinir la función get 
    def get_success_url(self):
        return reverse_lazy("login") + "?register"   
    
    # Redefinimos la función de get_form para cambiar el aspecto del formulario que es un poco malillo, el basico de django
    def get_form(self, form_class=None): 
        form = super(SignUpView, self).get_form()
        # Para mostrar en tiempo real, le cambio los tipos de los datos.
        # Los nombres de "username" "password1" y "password2" se miran en el codigo en ejecución, ya que en el fichero "signup" no se puede ver.
        form.fields["username"].widgets = forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Nombre de usuario"})
        form.fields["email"].widgets = forms.EmailInput(attrs={"class":"form-control mb-2"})
        form.fields["password1"].widgets = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Contraseña"})
        form.fields["password2"].widgets = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Repite la contraseña"})
    #   form.fields["username"].label  ....
        #Para cambiar las etiquetas, podriamos hacerlo aqui igual que con los cajetines hemos hecho (widgets)
        #form.fields["username"].label  ....
        #Pero no lo vamos hacer, porque los vamos a quitar entonces es más rápido ponerlo en la página "signup.html" en <style>
        return form 
    # No me funciona esta parte... (por eso lo hago en el ".html")


# Creamos una vista para la parte del "profile", la tabla de datos añadidos, (perfil de usuario) foto de avatar...
# Tenemos que decorar la clase porque no tiene sentido que exista un profile sin usuario, entonces
#tenemos que redefinir el metodo "dispatch"
@method_decorator(login_required, name="dispatch")
#class ProfileUpdate(TemplateView):    (lo cambiamos para que herede de UpdateView)
class ProfileUpdate(UpdateView):
#    model = Profile      # Le indicamos que tire del Profile que tenemos en ".models.py"  
#    fields = ["avatar", "bio", "link"]     # Y le indicamos los campos que queremos que tenga
    form_class = ProfileForm  # Lo cambiamos por el formulario que ahora hemos hecho "más mejor" en "forms.py"

    success_url = reverse_lazy("profile")  # Y le decimos que después redireccionamos a cargar la página de profile
    template_name = "registration/profile_form.html"

    #Pero necesitamos el "user" y la forma de conseguirlo es mediante el object y el request, no podemos pasarlo por el "path" porque lo podria ver todo el mundo
    #Entonces redefinimos el get de object
    def get_object(self):
        # recuperamos el objeto que se va a editar 
#       return  Profile.objects.get(user=self.request.user)   #Cambiamos el metodo "get" por "get_or_create", porque sino está creado el perfil, para que lo cree
#       return  Profile.objects.get_or_create(user=self.request.user)  #Pero no podemos devolverlo así tal cual, porque esta función
    # devuelve una tupla el profile y una variable "created" que te dice si se ha creado o no en este momento. 
        profile, create =  Profile.objects.get_or_create(user=self.request.user) 
        return profile   #Y ahora si devolvemos el perfil 
    

# Para hacer la vista del cambio de email, utilizo la anterior de Profile y cambio los campos
@method_decorator(login_required, name="dispatch")
class EmailUpdate(UpdateView):
    form_class = EmailForm  # formulario de "forms.py"
    success_url = reverse_lazy("profile")  # Y le decimos que después redireccionamos a cargar la página de profile
    template_name = "registration/profile_email_form.html"

    def get_object(self):
        return self.request.user  # Para hacer la recuperación del objeto
    
    def get_form(self, form_class=None): 
        form = super(EmailUpdate, self).get_form()
        # Para mostrar en tiempo real, le cambio los tipos de los datos.
        # Los nombres de "username" "password1" y "password2" se miran en el codigo en ejecución, ya que en el fichero "signup" no se puede ver.
        form.fields["email"].widgets = forms.EmailInput(
             attrs={"class":"form-control mb-2", "placeholder":"Email"})
        return form         # ponga lo que ponga no me funciona... 

   