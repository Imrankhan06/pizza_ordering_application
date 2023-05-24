from django_filters.rest_framework import DjangoFilterBackend
from django.urls import path
from orders.views import OrderListCreateView, OrderRetrieveUpdateDeleteView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDeleteView.as_view(), name='order-retrieve-update-delete'),
]
