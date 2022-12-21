# Salvator
Your medical records on the go


# API DOCUMENTATION

### BASE URL
http://web-02.feranmi.tech

### ROUTES

POST    /register : creates a new user (username and password are sent in json format)

```
a_oluwaferanmi@Young-Sahaba:~$ curl -X POST http://127.0.0.1:5000/api/v1/register -H "Content-Type: application/json" -d '{"username": "Ajayi", "password": "Ajayi2001"}

{
  "__class__": "UserLogin",
  "created_at": "2022-12-21T12:58:13.283570",
  "id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
  "password": "Ajayi2001",
  "updated_at": "2022-12-21T12:58:13.283614",
  "username": "Ajayi"
}

a_oluwaferanmi@Young-Sahaba:~$ curl -X POST http://127.0.0.1:5000/api/v1/register -H "Content-Type: application/json" -d '{"username": "Alabi", "password": "Alabi2001"}'

{
  "__class__": "UserLogin",
  "created_at": "2022-12-21T12:58:13.283570",
  "id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
  "password": "Alabi2001",
  "updated_at": "2022-12-21T12:58:13.283614",
  "username": "Alabi"
}

```

GET      /users : returns all Salvator users
```

a_oluwaferanmi@Young-Sahaba:~$ curl -X GET http://127.0.0.1:5000/api/v1/users

[
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-21T13:04:57",
    "id": "687d883c-9630-4a26-bfdb-48e0de5502db",
    "password": "Alabi2001",
    "updated_at": "2022-12-21T13:04:57",
    "username": "Alabi"
  },
  
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-21T12:58:13",
    "id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
    "password": "Ajayi2001",
    "updated_at": "2022-12-21T12:58:13",
    "username": "Ajayi"
  }
]

```

POST    /login : username and password are sent as json and it returns the medical records and biodta of that user

