# Endpoints 

## send-message


### How to use 
This endpoint is the one that implements the requested functionality. 

![imagen](https://github.com/user-attachments/assets/f99e75f7-47c2-4e4a-a08f-8b569283596b)

It is of type POST, and the payload must have the below data 

![imagen](https://github.com/user-attachments/assets/24704770-2cc6-46a5-b5cc-56141056cff1)

One key of message_category, which can have one of the categories in the DB (sports, finance, films)
and the contents of the message to be sent to the subscribed users of that category.

## Tests

It also has some tests which populate data inside the test itself and makes some comparison for the happy path and also one error scenario.

## Load data for testing

TO upload more data the django admin page can be used: 

http://127.0.0.1:8000/admin

the user is: apiuser
the password: adiviname001

or it already has some data populated which can be reuploaded again by using the command:

python manage.py loaddata input_data_fixture.json



