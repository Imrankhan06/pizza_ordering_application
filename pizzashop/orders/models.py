from django.db import models


class PizzaFlavor(models.Model):
    """Represents a flavor of pizza.

    Attributes:
        flavor (str): The name of the pizza flavor.

    """
    FLAVOR_CHOICES = [
        ('margarita', 'Margarita'),
        ('marinara', 'Marinara'),
        ('salami', 'Salami'),
    ]
    flavor = models.CharField(max_length=50, choices=FLAVOR_CHOICES)


class PizzaSize(models.Model):
    """Represents a size option for pizza.

    Attributes:
        size (str): The name of the pizza size.

    """
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)


class Customer(models.Model):
    """Represents a customer who places pizza orders.

    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
        phone_number (str): The phone number of the customer.

    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Represents a pizza order placed by a customer.

    Attributes:
        flavors (ManyToManyField): The flavors of the ordered pizzas.
        sizes (ManyToManyField): The sizes of the ordered pizzas.
        customer (ForeignKey): The customer who placed the order.
        delivery_status (str): The status of the order delivery.
        quantity (PositiveIntegerField): The number of pizzas for the order.

    """
    flavors = models.ManyToManyField(PizzaFlavor)
    sizes = models.ManyToManyField(PizzaSize)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
