from django.urls import path
from .views import inicial, platoXCate

urlpatterns = [
    path("", inicial, name="inicial"),

    path('platoXCate/<int:category_id>/', platoXCate, name="platoXCate"),  
]