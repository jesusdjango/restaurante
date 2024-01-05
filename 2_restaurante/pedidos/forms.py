from django import forms
from .models import Pedido 

class PedidoForm(forms.ModelForm):

    class Meta:                 # Basicamente para asignarle valor al estado, al inicio.
        model = Pedido

        fields = ["name", "platos", "estado", "total"]

        widgets = {   
            "name": forms.TextInput(attrs={'class':'form-control', }),  #"placeholder":"Escribe tu nombre"
            "estado": forms.TextInput(attrs={'value':'en proceso', "hidden":"true"}), 
            #"total": forms.DecimalField(attrs={"hidden":"true"})
        }

        # Esto para borrar las etiquetas, las igualamos a vacio
        labels = {
            "name":"", "platos":"", "estado":""
        }
