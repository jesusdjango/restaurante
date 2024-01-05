from django import forms   # Importación de formularios
from django.contrib.auth.forms import UserCreationForm # El modelo concreto creo que es
from django.contrib.auth.models import User # Modelo de usuario concreto
from .models import Profile

class MiFormularioEmail(UserCreationForm): #required es que es campo obligatorio. Entiendo que el siguiente es la ayuda...
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres de máximo y debe ser valido.")
    
    class Meta:
        model = User          # Aqui hemos añadido el campo "email", porque en la extructura interior de "User" existe, sino no podriamos utilizarlo y no funcionaria. (vaya que no me puedo inventar yo el nombre que me de la gana)
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):  #Creamos este metodo para validar el email y ver que no está ya en BBDD (se tiene que llamar así)
        miEmail = self.cleaned_data.get("email") # recuperamos en esta variable el valor que se ha introducido en el formulario
        if User.objects.filter(email=miEmail).exists():  #Si es igual a alguno de la BBDD sms
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return miEmail # Sino entra dentro del if devuelve el valor como correcto... 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ["avatar", "bio", "link"]  # Lo cogemos de la vista que tenemos en "views.py"
        widgets = { # Este dato "ClearableFileInput" quiere decir que se puede limpiar, por eso podemos limpiarlo en el formulario, nos da la opción.
            # Como siempre "Form-control-file" estará en algún fichero que yo no tengo...
            "avatar": forms.ClearableFileInput(attrs={"class":"Form-control-file mt-3"}),
            "bio": forms.Textarea(attrs={"class":"Form-control mt-3", "rows":4, "placeholder":"Biografía"}),
            "link": forms.URLInput(attrs={"class":"Form-control mt-3", "placeholder":"Enlace"}),
        }

class EmailForm(forms.ModelForm): #Declaramos el email como hemos hecho arriba en "MiFormularioEmail"
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres de máximo y debe ser valido.")

    class Meta:
        model = User  #Para que coja de la clase de User. Como hacemos también arriba.
        fields = ["email"]
        
    # Tenemos que hacer validaciones del email, y no valen las que tenemos arriba, ya que antes no existia,
    #entonces tenemos que ver si se ha modificado con respecto al que estaba antes y si se ha modificado entonces
    #ahora ya sí, comprobamos que no exista ya otro igual en la BBDD

    def clean_email(self):  #Creamos este metodo para validar el email y ver que no está ya en BBDD (se tiene que llamar así)
        miEmail = self.cleaned_data.get("email") # recuperamos en esta variable el valor que se ha introducido en el formulario
        if "email" in self.changed_data: #entonces tenemos que ver si se ha modificado con respecto al que estaba antes
            if User.objects.filter(email=miEmail).exists():  #Si es igual a alguno de la BBDD sms
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return miEmail # Sino entra dentro del if devuelve el valor como correcto...    
    
    