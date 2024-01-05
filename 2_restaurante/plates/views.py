#from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic.list import ListView  #Segunda parte que te devuelve una lista de paginas
from django.views.generic.detail import DetailView #Tercera parte para la vista individual
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plate

from django.urls import reverse, reverse_lazy
#from .forms import PageForm   #Mirar esto... 
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required # Para decorar el Mixin. También existe la opción de "login_required", "permission_required"
from django.utils.decorators import method_decorator #django nos obliga a utilizar este metodo para decorar


#Declaramos esta clase de tipo generico para poder reutilizarla en los apartados de "create", "update", "delete"
#Hacer Esto es un Mixins, lo que he dicho arriba.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required) # Esto hace lo mismo que el if...
    def dispatch(self, request, *args, **kwargs):
#        if not request.user.is_staff:
#            return redirect(reverse_lazy("admin:login"))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# (que devuelve una lista)  "plate_list.html"
class PlateListView(ListView):
    model = Plate

#(va a devolver solo un elemento)
class PlateDetailView(DetailView):
    model = Plate

#Clase para Crear, añadir un reg
@method_decorator(staff_member_required, name="dispatch") #Decoro la función para quitar el Mixin "StaffRequiredMixin"
class PlateCreate(CreateView):       
    model = Plate       

# (OJO, QUE LO MISMO TENGO QUE CAMBIARLO A FORMULARIO TAMBIÉN )
    fields = ["name", "categories", "price"]   
#   form_class = PageForm    (para utilizar el formulario)

    success_url = reverse_lazy("plates:plates") # Decimos que cuando termine vuelva a la página del listado de platos


@method_decorator(staff_member_required, name="dispatch")   #Decoro la función para quitar el Mixin "StaffRequiredMixin"
class PlateUpdate(UpdateView):        # Y así puedo dejarlo como estaba
    model = Plate

# (OJO, QUE LO MISMO TENGO QUE CAMBIARLO A FORMULARIO TAMBIÉN )
    fields = ["name", "categories", "price"]   
#   form_class = PageForm

    template_name_suffix = "_update_form" #Se utiliza este sufijo por defecto, para poner otro formulario (entiendo que de actualización)
    # Para que vuelva a su misma página
 
    success_url =  reverse_lazy("plates:plates")

@method_decorator(staff_member_required, name="dispatch")   
class PlateDelete(DeleteView):      
    model = Plate
    success_url =  reverse_lazy("plates:plates") # Le ponemos como en la creación que vaya a la página principal.

