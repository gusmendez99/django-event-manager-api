# Baby Events API

Basic baby events API made with Django Rest Framework, with Auth/JWT.

## Installation

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

And then, install all dependencies

```bash
pip install -r requirements.txt
```

Finally, run server on localhost:8000
```bash
python manage.py runserver
```

*Optional (already done). Run this command to add dummy data in the DB.
```bash
python manage.py shell < initialize.py
```

## Data

Data has been already stored in DB. So, assume this data.

*  Parent: mario (Mario Gomez, pw: mario1234)

   * Baby (id: 1): Maria Gomez 
   
        * Event (id: 3): Pee

        * Event (id: 4): Poop


   * Baby (id: 2): Lupita Gomez

        * Event (id: 2): Eat 


* Parent: julio (Julio Hernandez, pw: julio1234) 

   * Baby (id: 3): Rosa Hernandez

        * No events yet
   
   * Baby (id: 4): Fernando Hernandez

        * Event (id: 1): Poop 

## Usage
I recommend test this code via cURL from terminal.

1. Get token
```bash
    curl --location --request POST 'http://baby-events-api.herokuapp.com/api/v1/token-auth/' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=julio' \
    --data-urlencode 'password=julio1234'
```
2. Refresh token
```bash
    curl --location --request POST 'http://baby-events-api.herokuapp.com/api/v1/token-refresh/' \
    --data-urlencode 'token=token_to_refresh'
```
3. Get all babies of given parent 
```bash
    curl --location --request GET 'http://baby-events-api.herokuapp.com/api/v1/parents/2/babies' \
    --header 'Authorization: JWT insert_token_here'
```
4. Get single baby (if auth parent owns)
```bash
    curl --location --request GET 'http://baby-events-api.herokuapp.com/api/v1/babies/4' \
    --header 'Authorization: JWT insert_token_here'
```
5. Get all baby events (if auth parent owns)
```bash
    curl --location --request GET 'http://baby-events-api.herokuapp.com/api/v1/babies/4/events' \
    --header 'Authorization: JWT insert_token_here'
```
6. Add event to baby (if auth parent owns)
```bash
    curl --location --request POST 'http://baby-events-api.herokuapp.com/api/v1/events/' \
    --header 'Authorization: JWT insert_token_here' \
    --data-urlencode 'type=pee' \
    --data-urlencode 'description=Pee a lot' \
    --data-urlencode 'baby=3'
```
7. Get single baby (if auth parent owns)
```bash
    curl --location --request GET 'http://baby-events-api.herokuapp.com/api/v1/events/1' \
    --header 'Authorization: JWT insert_token_here'
```
8. Add new baby
```bash
    curl --location --request POST 'http://baby-events-api.herokuapp.com/api/v1/babies/' \
    --header 'Authorization: JWT insert_token_here' \
    --data-urlencode 'first_name=Ruben' \
    --data-urlencode 'last_name=Hernandez' \
    --data-urlencode 'age=1' \
    --data-urlencode 'parent=1'
```
9.  Get all babies 
```bash
    curl --location --request GET 'http://baby-events-api.herokuapp.com/api/v1/babies' \
    --header 'Authorization: JWT insert_token_here'
```

- Note: <em>replace token_to_refresh</em> and  <em>insert_token_here</em> .


## License
[MIT](https://choosealicense.com/licenses/mit/)