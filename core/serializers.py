from .models import Client, User, Address
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address_id', 'created_at', 'updated_at', 'active']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'birthdate', 'cpf', 'client_id', 'address_id', 'created_at', 'updated_at', 'active']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user_id', 'is_main', 'created_at', 'updated_at', 'active']
