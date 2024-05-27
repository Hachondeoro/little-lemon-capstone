from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=10)
        Menu.objects.create(title="Pizza", price=100, inventory=10)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-items')
        response = client.get(url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)