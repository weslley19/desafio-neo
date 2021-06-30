from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField('Atualizado em', auto_now=False, auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)


class Client(Base):
    name = models.CharField('Nome', max_length=255, blank=False)
    address_client = models.CharField('Endereço', max_length=255, blank=False, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class User(Base):
    name = models.CharField('Nome', max_length=255)
    birthdate = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', max_length=15, unique=True)
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Address(Base):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, blank=True)
    local = models.CharField('Local', max_length=255, default='')
    is_main = models.BooleanField('Endereço Principal?')

    def __str__(self):
        return self.local

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
