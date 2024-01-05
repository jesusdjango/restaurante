"""
URL configuration for restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views 
from django.conf.urls.static import static
from plates.urls import plates_padre
from categos.urls import categos_padre
from django.conf import settings 
from pedidos.urls import pedidos_padre

urlpatterns = [
    path("", include("core.urls")),

    path('categos/', include(categos_padre)), 

    path('plates/', include(plates_padre)), 

    # Metemos los path de "Auth" -> autenticación 
    path("accounts/", include("django.contrib.auth.urls")), 
    #Con esto te mete 8 urls que ya no tienes que definir --> login, logout, password_change, password_change_done, 
    #password_reset, password_reset_done, password_reset-confirm, password_reset_complete
    
    # Ahora creo el path para que se registren los usuarios, en principio con la misma raiz...
    path("accounts/", include("registration.urls")), 

    path("pedidos/", include(pedidos_padre)), 

    path('admin/', admin.site.urls),
]


# Y si estamos en modo prueba, añadimos (concatenamos) la ruta imagenes que están en static con sus Variables o Constantes configuradas en el fichero "settings.py"
if settings.DEBUG:   
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    