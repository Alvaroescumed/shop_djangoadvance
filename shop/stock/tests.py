from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import Group as DjangoGroup
from rest_framework.authtoken.models import Token

class UserCreationTestCase(APITestCase):

    def setUp(self):

        # creamos el usuario y lo añadimos al grupo gerentes
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.gerente_group, created = DjangoGroup.objects.get_or_create(name='Gerentes')
        self.user.groups.add(self.gerente_group)
        self.user.save()

        # creamos una categoría y un producto paro los test que dependen de los ids
        self.category = Category.objects.create(name="Test category")
        self.product = Product.objects.create(
            name="Test Product",
            description="test description",
            price=1,
            category=self.category
        )

    # comprobamos que los gerentes puedan crear productos/categorias/inventarios
    def test_product_creation(self):
        data = {
            "name" : "Camiseta estampada",
            "description" : "Camiseta de algodon estampada en motivos florales",
            "price" : 16,
            "category" : self.category.id
        }
        res = self.client.post('/api/products/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_category_creation(self):
        data = {
            "name" : "Accesories"
        }

        res = self.client.post('/api/category/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_inventory_creation(self):
        data = {
            "product" : self.product.id,
            "quantity": 100
        }

        res = self.client.post('/api/inventory/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    # Comprobamos que los usuarios no autenticados no puedan acceder a estos
    def test_product_creation_no_auth(self):
        self.client.force_authenticate(user=None)
        data = {
            "name" : "Camiseta estampada",
            "description" : "Camiseta de algodon estampada en motivos florales",
            "price" : 16,
            "category" : 2
        }

        res = self.client.post('/api/products/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_creation_no_auth(self):
        self.client.force_authenticate(user=None)
        data = {
            "name" : "Accesories"
        }

        res = self.client.post('/api/category/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_inventory_creation_no_auth(self):
        self.client.force_authenticate(user=None)
        data = {
            "product" : self.product.id,
            "quantity": 100
        }

        res = self.client.post('/api/inventory/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_inventory_read_no_auth(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/api/inventory/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_read_no_auth(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/api/category/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_product_read_no_auth(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/api/products/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    
# Creamos tambien algunos test para comprobar las funciones de los staff
class StaffCreationTest(APITestCase):
    
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+ self.token.key)
        self.staff_group, created = DjangoGroup.objects.get_or_create(name='Staff')
        self.user.groups.add(self.staff_group)
        self.user.save()

        self.category = Category.objects.create(name="Test category")
        self.product = Product.objects.create(
            name="Test Product",
            description="test description",
            price=1,
            category=self.category
        )
       
    def test_inventory_read_staff(self):
        res = self.client.get('/api/inventory/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_category_read_staff(self):
        res = self.client.get('/api/category/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_product_read_staff(self):
        res = self.client.get('/api/products/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_product_cant_create_staff(self):
        data = {
            "name" : "Camiseta estampada",
            "description" : "Camiseta de algodon estampada en motivos florales",
            "price" : 16,
            "category" : self.category.id
        }
        res = self.client.post('/api/products/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_inventory_creation(self):
        data = {
            "product" : self.product.id,
            "quantity": 100
        }

        res = self.client.post('/api/inventory/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
    




