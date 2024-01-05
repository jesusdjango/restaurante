from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Cargamos los modelos que vamos a querer probar

# Create your tests here.
class ProfileTestCase(TestCase):
    #   Metodo setUp que se hereda de TestCase, es donde tenemos que preparar la prueba, utilizamos el objeto "User" y le damos valores para crear uno, (inventado, es una prueba)
    #y con la función "create_user" vamos a crear un usuario, con nombre "test", correo, y password
    def setUp(self):
        User.objects.create_user("test", "test@test.com", "test1234")
        
    
    #Y esto es la propia prueba en si, puede llamarse como queramos, pero tiene que empezar siempre por "test_"
    def test_profile_exits(self):
        exists = Profile.objects.filter(user__username="test").exists()   # Te dice si hay un objeto en Profile que tenga de nombre "test", devuelve un boolean
        self.assertEqual(exists, True)  # te dice que para que sea igual o valido, la variable "exists" tiene que ser igual a true
    

