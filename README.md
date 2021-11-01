# JWT Authentication

## How to create Token?

### Obtain Token
$ http POST http://127.0.0.1:8000/gettoken/ username=username password=password

### Verify Token
$ http POST http://127.0.0.1:8000/verifytoken/ token=access_token

### Refresh Token
$ http POST http://127.0.0.1:8000/refreshtoken/ refresh=refresh_token


## How to send requests?

### GET Request
$ http GET http://127.0.0.1:8000/student/ 'Authorization: Bearer access_token'

### GET 1 Instance
$ http GET http://127.0.0.1:8000/student/1/ 'Authorization: Bearer access_token'

### POST Request
http -f POST http://127.0.0.1:8000/student/ name=Ritesh roll=123 city=Perth 'Authorization: Bearer access_token'

### PUT Request
$ http PUT http://127.0.0.1:8000/student/3/ name=Nisha roll=321 city=Perth 'Authorization: Bearer access_token'

### PATCH Request
$ http PATCH http://127.0.0.1:8000/student/3/ name=Manisha 'Authorization: Bearer access_token'

### DELETE Request
$ http DELETE http://127.0.0.1:8000/student/3/ 'Authorization: Bearer access_token'
