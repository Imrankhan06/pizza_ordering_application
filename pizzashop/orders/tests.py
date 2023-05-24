from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PizzaFlavor, PizzaSize, Customer, Order


class OrderAPITests(APITestCase):
    """Test case for the Order API endpoints."""
    def setUp(self):
        """Test case setup method."""
        self.flavor1 = PizzaFlavor.objects.create(flavor='margarita')
        self.flavor2 = PizzaFlavor.objects.create(flavor='marinara')
        self.size = PizzaSize.objects.create(size='medium')
        self.customer = Customer.objects.create(name='John Doe', address='123 Main St', phone_number='555-1234')

        self.order = Order.objects.create(customer=self.customer, delivery_status='pending', quantity=2)
        self.order.flavors.set([self.flavor1, self.flavor2])
        self.order.sizes.set([self.size])

    def test_list_orders(self):
        """Test the list orders API endpoint."""
        url = reverse('order-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_order(self):
        """Test the retrieve order API endpoint."""
        url = reverse('order-retrieve-update-delete', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.order.id)

    def test_create_order(self):
        """Test the create order API endpoint."""
        url = reverse('order-list-create')
        data = {
            'flavors': [{'flavor': 'salami'}],
            'sizes': [{'size': 'large'}],
            'customer': {
                'name': 'Jane Smith',
                'address': '456 Elm St',
                'phone_number': '555-5678'
            },
            'delivery_status': 'pending',
            'quantity': 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_update_order(self):
        """Test the update order API endpoint."""
        url = reverse('order-retrieve-update-delete', args=[self.order.id])
        data = {
            'flavors': [{'flavor': 'margarita'}, {'flavor': 'salami'}],
            'sizes': [{'size': 'small'}, {'size': 'large'}],
            'customer': {
                'name': 'John Doe',
                'address': '123 Main St',
                'phone_number': '555-1234'
            },
            'delivery_status': 'delivered',
            'quantity': 4
        }
        response = self.client.put(url, data, format='json')
        updated_order = Order.objects.get(id=self.order.id)
        self.assertEqual(updated_order.quantity, 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order_disallowed_status(self):
        """Test updating an order with a disallowed delivery status."""
        order = Order.objects.create(
            customer=self.customer,
            delivery_status='delivered',
            quantity=2
        )
        order.flavors.set([self.flavor1, self.flavor2])
        order.sizes.set([self.size])

        updated_data = {
            'delivery_status': 'pending',
        }

        url = reverse('order-retrieve-update-delete', args=[order.id])
        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Refresh the order from the database
        order.refresh_from_db()

        self.assertEqual(order.delivery_status, 'delivered')
