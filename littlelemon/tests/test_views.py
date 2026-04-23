from django.test import TestCase
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Bruschetta", price=15, inventory=50)
        Menu.objects.create(title="Pasta", price=25, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_data)
