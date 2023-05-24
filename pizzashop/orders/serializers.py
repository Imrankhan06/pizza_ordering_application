from rest_framework import serializers
from .models import PizzaFlavor, PizzaSize, Customer, Order


class PizzaFlavorSerializer(serializers.ModelSerializer):
    """Serializer for the PizzaFlavor model.

    Fields:
        flavor (str): The name of the pizza flavor.

    """
    class Meta:
        model = PizzaFlavor
        fields = ['flavor']


class PizzaSizeSerializer(serializers.ModelSerializer):
    """Serializer for the PizzaSize model.

    Fields:
        size (str): The name of the pizza size.

    """
    class Meta:
        model = PizzaSize
        fields = ['size']


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for the Customer model.

    Fields:
        name (str): The name of the customer.
        address (str): The address of the customer.
        phone_number (str): The phone number of the customer.

    """
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model.

    Fields:
        id (int): The ID of the order.
        flavors (list): The flavors of the ordered pizzas.
        sizes (list): The sizes of the ordered pizzas.
        customer (dict): Information about the customer who placed the order.
        delivery_status (str): The status of the order delivery.
        quantity (int): The number of pizzas for the order.

    """
    flavors = PizzaFlavorSerializer(many=True)
    sizes = PizzaSizeSerializer(many=True)
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'flavors', 'sizes', 'customer', 'delivery_status', 'quantity']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create and return a new Order instance."""
        flavors_data = validated_data.pop('flavors', [])
        sizes_data = validated_data.pop('sizes', [])
        customer_data = validated_data.pop('customer', {})
        quantity = validated_data.pop('quantity', 1)

        flavors = [PizzaFlavor.objects.get_or_create(flavor=flavor_data['flavor'])[0] for flavor_data in flavors_data]
        sizes = [PizzaSize.objects.get_or_create(size=size_data['size'])[0] for size_data in sizes_data]

        customer = Customer.objects.create(
            name=customer_data.get('name'),
            address=customer_data.get('address'),
            phone_number=customer_data.get('phone_number')
        )

        order = Order.objects.create(
            customer=customer,
            delivery_status=validated_data.get('delivery_status')
        )
        order.flavors.set(flavors)
        order.sizes.set(sizes)
        order.quantity = quantity

        return order

    def update(self, instance, validated_data):
        """Update and return an existing Order instance."""
        flavors_data = validated_data.pop('flavors', [])
        sizes_data = validated_data.pop('sizes', [])
        customer_data = validated_data.pop('customer', {})
        quantity = validated_data.pop('quantity', instance.quantity)

        flavors = [PizzaFlavor.objects.get_or_create(flavor=flavor_data['flavor'])[0] for flavor_data in flavors_data]
        sizes = [PizzaSize.objects.get_or_create(size=size_data['size'])[0] for size_data in sizes_data]

        instance.customer.name = customer_data.get('name', instance.customer.name)
        instance.customer.address = customer_data.get('address', instance.customer.address)
        instance.customer.phone_number = customer_data.get('phone_number', instance.customer.phone_number)
        instance.customer.save()

        instance.flavors.set(flavors)
        instance.sizes.set(sizes)

        # Check if the delivery status allows updates
        disallowed_statuses = ['delivered']  # Add other disallowed statuses if needed
        if instance.delivery_status in disallowed_statuses:
            raise serializers.ValidationError("Order cannot be updated for the current delivery status.")

        instance.delivery_status = validated_data.get('delivery_status', instance.delivery_status)
        instance.quantity = quantity
        instance.save()

        return instance
