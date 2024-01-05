#from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic.list import ListView  #Segunda parte que te devuelve una lista de paginas
from django.views.generic.detail import DetailView #Tercera parte para la vista individual
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pedido
from .forms import PedidoForm
from django.shortcuts import render

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
    
    
@method_decorator(staff_member_required, name="dispatch") 
class PedidoListView(ListView):
    model = Pedido


#(va a devolver solo un elemento)
class PedidoDetailView(DetailView):

    model = Pedido

    def get_object(self):
        obj = super(PedidoDetailView, self).get_object()   #Recogemos el objeto
        total = 0
        for i in obj.platos.all():
            total += i.price 
        print("valor de total:", total)
        obj.total = total  
        return obj

  
#Clase para Crear, añadir un reg
class PedidoCreate(CreateView):       
    model = Pedido       

#   fields = ["name", "platos", "estado"]   
    form_class = PedidoForm    

 #   success_url =  reverse_lazy("pedidos:pedido", args=[self.object.id]) # Decimos que cuando termine vuelva a la página del listado de platos
    def get_success_url(self):
       return reverse_lazy("pedidos:pedido", args=[self.object.id]) + "?ok" 

@method_decorator(staff_member_required, name="dispatch")   #Decoro la función para quitar el Mixin "StaffRequiredMixin"
class PedidoUpdate(UpdateView):        # Y así puedo dejarlo como estaba
    model = Pedido

    fields = ["name", "estado"]   

    template_name_suffix = "_update_form" #Se utiliza este sufijo por defecto, para poner otro formulario (entiendo que de actualización)
   
    success_url =  reverse_lazy("pedidos:pedidos") # Le ponemos como en la creación que vaya a la página principal.


@method_decorator(staff_member_required, name="dispatch")   
class PedidoDelete(DeleteView):      
    model = Pedido
    success_url =  reverse_lazy("pedidos:pedidos") # Le ponemos como en la creación que vaya a la página principal.

