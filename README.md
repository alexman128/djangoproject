# How to run 
This project uses MySQL as the DB engine, so it must be installed first.
Also a new env should be created  

**python -m venv .venv**

and the environment must be activated  

**.\\.venv\Scripts\activate**

then the requirements must be installed with pip  

**pip install -r requirements.txt**

Go the the root folder of the project and run the below command  

**python manage.py runserver**

After running the program and if no errors ocurred, the main url and the port number are going to be shown in the terminal, 
this along with  the end point should be used to access the end point

![imagen](https://github.com/user-attachments/assets/774ebeec-1988-4684-a04c-7269b02fd918)

And then use a program like postman to send the request to the endpoint.

# Endpoints 

## send-message


### How to use 
This endpoint is the one that implements the requested functionality. 

![imagen](https://github.com/user-attachments/assets/f99e75f7-47c2-4e4a-a08f-8b569283596b)

It is of type POST, and the payload must have the below data 

![imagen](https://github.com/user-attachments/assets/24704770-2cc6-46a5-b5cc-56141056cff1)

One must provide one key of **message_category**, which can have one of the categories in the DB (sports, finance, films)
and **message_contents** which are the contents of the message to be sent to the subscribed users of that category.

Note: The actual message sending is not happening, it is being simulated by sending messages to the log, these log entries 
have enough info to identify the message such as the user, user id, message category, and message channel along with the time it was sent.

![imagen](https://github.com/user-attachments/assets/8ce0285a-ff74-4a76-b5e4-c2810d2c3067)


## Tests

It also has some tests which populate data inside the test itself and makes some comparison for the happy path and also one error scenario.

In order to run the tests the below command must be entered at the root of the project directory: 

(It is assumed that the server is running with the command "**python manage.py runserver**" in another terminal)

**python manage.py test notification.tests**

![imagen](https://github.com/user-attachments/assets/e85d13aa-3b32-4c54-b49d-d4ac0d143706)


## Load data for testing

TO upload more data the django admin page can be used: 

http://127.0.0.1:8000/admin

the user is: **apiuser** \
the password: **adiviname001**

![imagen](https://github.com/user-attachments/assets/601215b4-bb86-4d14-ad30-c3c268a92102)

![imagen](https://github.com/user-attachments/assets/354a37c4-3236-4347-854b-e72e732f1c40)

![imagen](https://github.com/user-attachments/assets/f623a8dd-8804-407b-a880-5e301afdfe1d)

![imagen](https://github.com/user-attachments/assets/688a940d-40cb-40a4-9d21-a6aad83fac35)





or it already has some data populated which can be reuploaded again by using the command:

**python manage.py loaddata input_data_fixture.json**


# Design pattern 

The design pattern used is the **Strategy pattern** which as used to select the channel type to write to

and the following classes implement it: 

- AbstractChannel
- SMSChannel
- PushChannel
- EmailChannel

and the context is the class: 

- MessageSender

Also Django already provides their own implementation of the **MVC** pattern which is the **Model** **View** **Template** pattern


# Database and Models

The Database used is MySQL which was required in order to implement the foreign keys and many to many relations in DJANGO ORM

MYSQL Users and passwords

- User: root Password: welcome
- User: alexman Password: welcome


Command to enter the db 

mysql -u alexman -p 
(It will ask for a password) 

then you can see the databases 

![imagen](https://github.com/user-attachments/assets/7543f5af-bb6b-489e-ac51-559fc06f2ecc)

Then you can see the tables 

![imagen](https://github.com/user-attachments/assets/1b266498-a97f-48bb-a024-55f6e3b16577)

Then you can see the data of the application: 

![imagen](https://github.com/user-attachments/assets/8312b822-9015-48ad-9437-63e71ea6b81c)



![imagen](https://github.com/user-attachments/assets/ff2ef75d-355a-46b7-97e0-39d2a0f0a013)






