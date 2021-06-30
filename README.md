# Documentação da API

Documentação de uso da API.

Para acessar os endpoints que necessitam de autorização, envie no header da requisição o `Token de acesso` com o prefixo `Bearer`, por exemplo: 

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
 

## ENDPOINTS

*Cliente*
- [**Create**](#criar): /api/client/
- [**Update**](#atualizar): /api/client/{id}/
- [**ListAllClients**](#dados-de-todos-os-clientes): /api/client/
- [**ListClient**](#cliente-especifico): /api/client/{id}/
- [**Delete**](#deletar): /api/client/{id}/

*Usuário*
- [**Create**](#criar): /api/user/
- [**Update**](#atualizar): /api/user/{id}/
- [**ListAllUsers**](#dados-de-todos-os-usuarios): /api/user/
- [**ListUser**](#usuario-especifico): /api/user/{id}/
- [**Delete**](#deletar): /api/user/{id}/

*Endereço*
- [**Create**](#criar): /api/address/
- [**Update**](#atualizar): /api/address/{id}/
- [**GetAllAddress**](#dados-de-todos-os-address): /api/address/
- [**GetAddress**](#address-especifico): /api/address/{id}/
- [**Delete**](#deletar): /api/address/{id}/


## Acesso

### Login

O login precisa de dois campos `username` e `password`.

- Endpoint: **/api/login/**
- Allowed method: POST
 
Para fazer login do usuário no sistema envie um POST ao endpoint e no corpo da requisição forneça as credencias do usuário tentando acessar o sistema nos campos `username` e `password`.

*POST*:

Corpo da requisição: JSON

```JSON
{
  "username": "login",
  "password": "senha",
}
```

Resposta:

*status_code*: 200
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF..."
}
```

- `access`: Token utilizado como Authorization para acessar rotas privadas.
- `refresh`: Token com um tempo de vida maior para atualizar o Token de acesso.

### Refresh

- Endpoint: **/api/token/refresh/**
- Allowed method: POST
 
Para fazer gerar um novo token de acesso para um usuário sem precisar passar pela rota de Login novamente, você pode fazer uma requisição ao endpoint de refresh para receber um token novo de acesso e refresh com tempo de vida estendido. 

*Importante*: O token de `refresh` deve ser um token válido, ou seja, não pode ter expirado. Por esse motivo ele tem um tempo de vida maior do que o token de acesso.

Para renovar o Token, forneça os tokens de `access` e `refresh` atuais do usuário.

*POST*:

Corpo da requisição: JSON

```JSON
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF...",
}
```

Resposta:

*status_code*: 200
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwI...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b20cmVmcmVzaCIsImV4cCI6MTU4NTEzF..."
}
```

- `access`: Token utilizado como Authorization para acessar rotas privadas.
- `refresh`: Token com um tempo de vida maior para atualizar o Token de acesso.


### Dados do usuário:

O endpoint de dados do usuário é útil para pegar os dados como *nome*, *data de nascimento*, entre outros dados referentes ao usuário vinculado ao token de acesso.

- Endpoint: **/api/user/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados do usuário deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso Bearer válido do usuário.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 6,
    "name": "Bob",
    "birthdate": "2000-04-04",
    "cpf": "342334",
    "client_id": 5,
    "created_at": "2021-06-29T22:01:34.272427-03:00",
    "updated_at": "2021-06-29T21:16:48.035644-03:00",
    "active": true
}
```

### Usuário especifico:

O endpoint para mostrar dados de um usuário em especifico é útil para pegar/atualizar os dados de um usuário como *nome*, *data de nascimento*, *cpf*, entre outros dados referentes ao usuário de id igual ao repassado na url.

- Endpoint: **/api/user/{user_id}/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados do usuário deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso JWT válido do usuário.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 6,
    "name": "Bob",
    "birthdate": "2000-04-04",
    "cpf": "342334",
    "client_id": 5,
    "created_at": "2021-06-29T22:01:34.272427-03:00",
    "updated_at": "2021-06-29T21:16:48.035644-03:00",
    "active": true
}
```


### Dados do cliente:

O endpoint de dados do cliente é útil para pegar os dados como *nome*, *local*, entre outros dados referentes ao cliente.

- Endpoint: **/api/client/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados do cliente deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso Bearer válido do cliente.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 5,
    "name": "Unimed Teresina02",
    "address_client": "Teresina",
    "created_at": "2021-06-29T21:11:10.904421-03:00",
    "updated_at": "2021-06-29T21:11:10.904476-03:00",
    "active": true
}
```

### Dados de endereço:

O endpoint de dados de endereço é útil para pegar os dados como *user_id*, *local*, *is_main* entre outros dados referentes ao endereço vinculado a um usuário

- Endpoint: **/api/address/**
- Allowed method: GET
- Authorization necessária

Para pegar os dados de endereço de um usuário deve ser feito uma requisição com o verbo http GET ao endpoint, e no header da requisição deve conter o campo de Authorization com o token de acesso Bearer válido do usuário.

*GET*:

Header

    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIi...

Resposta:

*status_code*: 200
```json
{
    "id": 7,
    "user_id": 6,
    "local": "Teresina",
    "is_main": true,
    "created_at": "2021-06-29T21:17:26.314467-03:00",
    "updated_at": "2021-06-29T21:17:26.314514-03:00",
    "active": true
}
```