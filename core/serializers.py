from .models import Client, User, Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user_id', 'local', 'is_main', 'created_at', 'updated_at', 'active']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address_client', 'created_at', 'updated_at', 'active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'birthdate', 'cpf', 'client_id', 'created_at', 'updated_at', 'active']
