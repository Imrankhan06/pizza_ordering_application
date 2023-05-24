from rest_framework import generics
from .models import PizzaFlavor, PizzaSize, Customer, Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    """API view for listing and creating orders.

    GET:
    List all orders.

    POST:
    Create a new order.

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """API view for retrieving, updating, and deleting an order.

    GET:
    Retrieve the details of an order.

    PUT:
    Update the details of an order.

    DELETE:
    Delete an order.

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
