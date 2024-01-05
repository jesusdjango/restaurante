from django.urls import path
#from plates.views import SampleplatesView  
from plates.views import PlateListView, PlateDetailView, PlateCreate, PlateUpdate, PlateDelete

plates_padre = ([  
    path("plates/", PlateListView.as_view(), name="plates"),   # devuelve una lista

    path('<int:pk>/', PlateDetailView.as_view(), name="plate"), 
  
    path("create/", PlateCreate.as_view(), name="create"),

   # pk  para que vaya a su propio plato concreto
    path("update/<int:pk>/", PlateUpdate.as_view(), name="update"),

    path("delete/<int:pk>/", PlateDelete.as_view(), name="delete"),

], "plates")  #Lo convertimos en tupla, ahora utilizamos siempre "plates:xxx" para llamarla

