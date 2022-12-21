# Salvator
Your medical records on the go


# API DOCUMENTATION

### BASE URL
http://web-02.feranmi.tech

### ROUTES
GET      /users : returns all Salvator users
`
curl -X GET web-02.feranmi.tech/api/v1/users

[
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-20T12:26:28",
    "id": "0d54712a-e1c8-44c2-a10c-22d0637d4b39",
    "password": "ade2001",
    "updated_at": "2022-12-20T12:26:28",
    "username": "bola"
  },
  
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-20T16:39:12",
    "id": "180f49c4-4ec1-4368-b9d3-459e5a783bda",
    "password": "Bamiji2001",
    "updated_at": "2022-12-20T16:39:12",
    "username": "Bamiji"
  }
  ]
  `
POST    /register : creates a new user (username and password are sent in json format)

POST    /login : username and password are sent as json and it returns the medical records and biodta of that user

