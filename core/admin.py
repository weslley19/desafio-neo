from django.contrib import admin
from .models import Address, Client, User


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'local', 'is_main')
    search_fields = ['local']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_client')
    search_fields = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'cpf', 'client_id')
    search_fields = ['name']
