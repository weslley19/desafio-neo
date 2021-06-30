from .models import Client, User, Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'local', 'is_main']


class ClientSerializer(serializers.ModelSerializer):
    # address = AddressSerializer(required=True)
    class Meta:
        model = Client
        fields = ['id', 'name', 'active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'birthdate', 'cpf', 'client_id', 'address_id', 'created_at', 'updated_at', 'active']
