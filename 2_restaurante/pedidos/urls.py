from django.urls import path
#from plates.views import SampleplatesView  
from pedidos.views import PedidoListView, PedidoDetailView, PedidoCreate, PedidoUpdate, PedidoDelete

pedidos_padre = ([  
    path("pedidos/", PedidoListView.as_view(), name="pedidos"),   # devuelve una lista

    path('<int:pk>/', PedidoDetailView.as_view(), name="pedido"), 
  
    path("create/", PedidoCreate.as_view(), name="create"),

   # pk  para que vaya a su propio plato concreto
    path("update/<int:pk>/", PedidoUpdate.as_view(), name="update"),

    path("delete/<int:pk>/", PedidoDelete.as_view(), name="delete"),

], "pedidos")  #Lo convertimos en tupla, ahora utilizamos siempre "pedidos:xxx" para llamarla

