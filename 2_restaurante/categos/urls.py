from django.urls import path
#from plates.views import SampleplatesView  
from categos.views import CategoListView, CategoDetailView, CategoCreate, CategoUpdate, CategoDelete

categos_padre = ([  
    path("categos/", CategoListView.as_view(), name="categos"),   # devuelve una lista

    path('<int:pk>/', CategoDetailView.as_view(), name="catego"), 
  
    path("create/", CategoCreate.as_view(), name="create"),

   # pk  para que vaya a su propio plato concreto
    path("update/<int:pk>/", CategoUpdate.as_view(), name="update"),

    path("delete/<int:pk>/", CategoDelete.as_view(), name="delete"),

], "categos")  #Lo convertimos en tupla, ahora utilizamos siempre "categos:xxx" para llamarla

