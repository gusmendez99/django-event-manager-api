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
I recommend test this code via CURL test online, here: https://reqbin.com/curl 

1. Get token
```bash
    curl
```
2. Refresh token
```bash
    curl
```
3. Get all babies of given parent 
```bash
    curl
```
4. Get single baby (if auth parent owns)
```bash
    curl
```
5. Get all baby events (if auth parent owns)
```bash
    curl
```
6. Add event to baby (if auth parent owns)
```bash
    curl
```
7. Get single baby (if auth parent owns)
```bash
    curl
```
8. Add new baby
```bash
    curl
```
9.  Get all babies 
```bash
    curl
```

- Note: from 3-9, needs Authorization header.


## License
[MIT](https://choosealicense.com/licenses/mit/)