from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField('Atualizado em', auto_now=False, auto_now_add=True)
    active = models.BooleanField('Ativo?')


class Client(Base):
    name = models.CharField('Nome', max_length=255)
    address_id = models.ForeignKey('Address', verbose_name='client_address', on_delete=models.CASCADE) 


class User(Base):
    name = models.CharField('Nome', max_length=255)
    birthdate = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', max_length=15, unique=True)
    client_id = models.ForeignKey('Client', verbose_name='user_client', on_delete=models.CASCADE)
    address_id = models.ForeignKey('Address', verbose_name='user_address', on_delete=models.CASCADE)


class Address(Base):
    user_id = models.ForeignKey('User', verbose_name='address_user', on_delete=models.CASCADE)
    is_main = models.BooleanField('Endereço Principal?')
