# Salvator
Your medical records on the go


# API DOCUMENTATION

### BASE URL
http://web-02.feranmi.tech

### ROUTES
/register : POST method only

POST    /register : creates a new user (username and password are sent in json format)

```
a_oluwaferanmi@Young-Sahaba:~$ curl -X POST http://127.0.0.1:5000/api/v1/register -H "Content-Type: application/json" -d '{"username": "Ajayi", "password": "Ajayi2001", "email": "Ajayi@gmail.com"}'

{
  "__class__": "UserLogin",
  "created_at": "2022-12-29T23:08:12.236690",
  "email": "Ajayi@gmail.com",
  "id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
  "password": "Ajayi2001",
  "updated_at": "2022-12-29T23:08:12.236734",
  "username": "Ajayi"
}

a_oluwaferanmi@Young-Sahaba:~$ curl -X POST http://127.0.0.1:5000/api/v1/register -H "Content-Type: application/json" -d '{"username": "Alabi", "password": "Alabi2001", "email": "Alabi@gmail.com"}'

{
  "__class__": "UserLogin",
  "created_at": "2022-12-29T23:11:12.892208",
  "email": "Alabi@gmail.com",
  "id": "4e70a859-c2fa-4c15-bd55-886eac4056de",
  "password": "Alabi2001",
  "updated_at": "2022-12-29T23:11:12.892252",
  "username": "Alabi"
}

```
/users : GET method only

GET      /users : returns all Salvator users
```

a_oluwaferanmi@Young-Sahaba:~$ curl -X GET http://127.0.0.1:5000/api/v1/users

[
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-29T23:11:13",
    "id": "4e70a859-c2fa-4c15-bd55-886eac4056de",
    "password": "Alabi2001",
    "updated_at": "2022-12-29T23:11:13",
    "username": "Alabi"
  },
  {
    "__class__": "UserLogin",
    "created_at": "2022-12-29T23:08:12",
    "id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
    "password": "Ajayi2001",
    "updated_at": "2022-12-29T23:08:12",
    "username": "Ajayi"
  }
]

```
/biodata/<username> : methods are POST, GET, PUT and DELETE

POST     /biodata/username : creates the biodata of a users
 
 GET    /biodata/username  : gets a user's biodata
 
 PUT    /biodata/username : updates a user's biodata
 
 DELETE /biodata/username : deletes's a user's biodata
 
```
a_oluwaferanmi@Young-Sahaba:~$ curl -X POST http://127.0.0.1:5000/api/v1/biodata/Ajayi -H "Content-Type: application/json" -d '{"first_name": "Ajayi", "last_name": "Omowon", "blood_group": "B+", "genotype": "AA", "age": 23, "weight": 64.5, "height": 1.75, "allergies": "Hay fever"}'
  
 
 {
  "__class__": "UserMedInfo",
  "age": 23,
  "allergies": "Hay fever",
  "blood_group": "B+",
  "created_at": "2022-12-21T13:26:53.510000",
  "first_name": "Ajayi",
  "genotype": "AA",
  "height": 1.75,
  "id": "7b081586-ea1c-4d4a-b91b-70e57bdfc6ea",
  "last_name": "Omowon",
  "med_id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
  "updated_at": "2022-12-21T13:26:53.510069",
  "weight": 64.5
}
  
  
 a_oluwaferanmi@Young-Sahaba:~$ curl -X GET http://127.0.0.1:5000/api/v1/biodata/Ajayi
  
  {
  "__class__": "UserMedInfo",
  "age": 23,
  "allergies": "Hay fever",
  "blood_group": "B+",
  "created_at": "2022-12-21T13:26:54",
  "first_name": "Ajayi",
  "genotype": "AA",
  "height": 1.75,
  "id": "7b081586-ea1c-4d4a-b91b-70e57bdfc6ea",
  "last_name": "Omowon",
  "med_id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
  "updated_at": "2022-12-21T13:26:54",
  "weight": 64.5
}
  
  
  a_oluwaferanmi@Young-Sahaba:~$ curl -X PUT http://127.0.0.1:5000/api/v1/biodata/Ajayi -H "Content-Type: application/json" -d '{"weight": 69.5, "height": 1.88}'
  
  {
  "__class__": "UserMedInfo",
  "age": 23,
  "allergies": "Hay fever",
  "blood_group": "B+",
  "created_at": "2022-12-21T13:26:54",
  "first_name": "Ajayi",
  "genotype": "AA",
  "height": 1.88,
  "id": "7b081586-ea1c-4d4a-b91b-70e57bdfc6ea",
  "last_name": "Omowon",
  "med_id": "bcb1d959-b3f2-4dca-9fd5-754ffc35bfe8",
  "updated_at": "2022-12-21T13:44:53.474191",
  "weight": 69.5
}
  
  a_oluwaferanmi@Young-Sahaba:~$ curl -X DELETE http://127.0.0.1:5000/api/v1/biodata/Ajayi
  
  "Deleted Successfully"
  
  a_oluwaferanmi@Young-Sahaba:~$ curl -X GET http://127.0.0.1:5000/api/v1/biodata/Ajayi
  
  "Record not found"
  
  ```
  
  POST :      /record/<username> :          creates a medical record
  
  ```
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X POST http://127.0.0.1:5000/api/v1/record/Ajayi -H "Content-Type: applica
tion/json" -d '{"date": "22/12/1930", "diagnosis": "Tuberculosis", "hospital": "healthtex hospital", "doctor_name": "Alalade Ajala", "doctor_contact": "Alalade@gmail.com", "prescription": "Pyrazinamide"}'

{
  "__class__": "Records",
  "created_at": "2022-12-29T23:24:17.918208",
  "date": "22/12/1930",
  "diagnosis": "Tuberculosis",
  "doctor_contact": "Alalade@gmail.com",
  "doctor_name": "Alalade Ajala",
  "hospital": "healthtex hospital",
  "id": "06cdd750-0613-4669-a13e-8ce7e00f414c",
  "prescription": "Pyrazinamide",
  "records_id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
  "updated_at": "2022-12-29T23:24:17.918269"
}


a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X POST http://127.0.0.1:5000/api/v1/record/Ajayi -H "Content-Type: applica
tion/json" -d '{"date": "22/12/1937", "diagnosis": "Diabetes", "hospital": "healthtex hospital", "doctor_name": "Alalade Ajala", "doctor_contact": "Alalade@gmail.com", "prescription": "Dialysis"}'
 
 {
  "__class__": "Records",
  "created_at": "2022-12-29T23:27:19.949803",
  "date": "22/12/1937",
  "diagnosis": "Diabetes",
  "doctor_contact": "Alalade@gmail.com",
  "doctor_name": "Alalade Ajala",
  "hospital": "healthtex hospital",
  "id": "d56a251e-d0b9-4eb0-8ce9-fb7c6a39b37d",
  "prescription": "Dialysis",
  "records_id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
  "updated_at": "2022-12-29T23:27:19.949858"
}

```
  
  GET          :   /records/<username> :   returns a list of a user's medical records
  ```
  
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X GET http://127.0.0.1:5000/api/v1/records/Ajayi
  
  [
  {
    "__class__": "Records",
    "created_at": "2022-12-29T23:24:18",
    "date": "22/12/1930",
    "diagnosis": "Tuberculosis",
    "doctor_contact": "Alalade@gmail.com",
    "doctor_name": "Alalade Ajala",
    "hospital": "healthtex hospital",
    "id": "06cdd750-0613-4669-a13e-8ce7e00f414c",
    "prescription": "Pyrazinamide",
    "records_id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
    "updated_at": "2022-12-29T23:24:18"
  },
  {
    "__class__": "Records",
    "created_at": "2022-12-29T23:27:20",
    "date": "22/12/1937",
    "diagnosis": "Diabetes",
    "doctor_contact": "Alalade@gmail.com",
    "doctor_name": "Alalade Ajala",
    "hospital": "healthtex hospital",
    "id": "d56a251e-d0b9-4eb0-8ce9-fb7c6a39b37d",
    "prescription": "Dialysis",
    "records_id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
    "updated_at": "2022-12-29T23:27:20"
  }
]
  
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X GET http://127.0.0.1:5000/api/v1/records/Alabi
  
  "You have no saved record"
  
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X POST http://127.0.0.1:5000/api/v1/record/Alabi -H "Content-Type: applica
tion/json" -d '{"date": "22/12/1957", "diagnosis": "Covid-19", "hospital": "healthtex hospital", "doctor_name": "Alalade
 Ajala", "doctor_contact": "Alalade@gmail.com", "prescription": "14-day isolation"}'
  
  {
  "__class__": "Records",
  "created_at": "2022-12-29T23:34:54.270889",
  "date": "22/12/1957",
  "diagnosis": "Covid-19",
  "doctor_contact": "Alalade@gmail.com",
  "doctor_name": "Alalade Ajala",
  "hospital": "healthtex hospital",
  "id": "12ea9d9c-9483-44c6-aa37-2748ec1ba511",
  "prescription": "14-day isolation",
  "records_id": "4e70a859-c2fa-4c15-bd55-886eac4056de",
  "updated_at": "2022-12-29T23:34:54.270945"
}
  
   a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X GET http://127.0.0.1:5000/api/v1/records/Alabi
  
  [
  {
    "__class__": "Records",
    "created_at": "2022-12-29T23:34:54",
    "date": "22/12/1957",
    "diagnosis": "Covid-19",
    "doctor_contact": "Alalade@gmail.com",
    "doctor_name": "Alalade Ajala",
    "hospital": "healthtex hospital",
    "id": "12ea9d9c-9483-44c6-aa37-2748ec1ba511",
    "prescription": "14-day isolation",
    "records_id": "4e70a859-c2fa-4c15-bd55-886eac4056de",
    "updated_at": "2022-12-29T23:34:54"
  }
]
  
  
  ```
  
  GET :      record/<id>/<username> : rettuns the medical record of the user with the specified id
  
  ```
  
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X GET http://127.0.0.1:5000/api/v1/record/d56a251e-d0b9-4eb0-8ce9-fb7c6a39b37d/Ajayi
  
  {
  "__class__": "Records",
  "created_at": "2022-12-29T23:27:20",
  "date": "22/12/1937",
  "diagnosis": "Diabetes",
  "doctor_contact": "Alalade@gmail.com",
  "doctor_name": "Alalade Ajala",
  "hospital": "healthtex hospital",
  "id": "d56a251e-d0b9-4eb0-8ce9-fb7c6a39b37d",
  "prescription": "Dialysis",
  "records_id": "f5868a41-0543-4a8b-a9c3-40a9e336b802",
  "updated_at": "2022-12-29T23:27:20"
}
  
  (with a fake id)
  a_oluwaferanmi@Young-Sahaba:~/Salvator$ curl -X GET http://127.0.0.1:5000/api/v1/record/f5868a41-0543-4a8b-a9c3-40a9e336b802/Ajayi
  
  "Record not found"
  
  ```

POST    /login : username and password are sent as json and it returns the medical records and biodta of that user

A user can login via username and password or email and password

```
via email and password

```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

