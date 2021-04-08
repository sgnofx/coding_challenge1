# coding_challenge1

The objective of login through an authenticator and redirecting back to client is done by using Django REST framework
Django REST framework makes it easy to create JWT token and provide methods for both verifying and creating the token.
In this project there are two apps
  1. challenge1 - This is the app where all the client related fuctions are made
  2. authenticator - This is the app where authenticator relatd functions are made

Client webpage - There is simple login link which will be redirected to authenticator, along with parameteres such as client_id and return_uri
Authenticator webpage - it will check various conditions and a login form will be displayed for entering the credentials
Credentials to be enetered - username: yash, password: abcd
After this we will be redirected to client page with username displayed

STEPS FOR RUNNING THE SERVER:
1. install required libraries, there is requirement.txt file which can be used to install required libraries by command "pip install -r requirements.txt"
2. run command "django migrate" (this will install the databse required for login)
3. run command "django makemigrations"
4. after successfull installation run the server by command (make sure you are in the directory where manage.py is stored before running this command) : python manage.py runserver
5. then go the specified URL (mostly http://127.0.0.1:8000/)
6. then click on login
7. nter credentials as (username: yash, password: abcd) on login page
8. if the error for invalid username comes inspite of doing migrations then do following:
  1. run command python manage.py createsuperuser
  2. it will ask for username and password
  3. enter username and password as mentioned above
  4. then try login in

Some screenshots of the flow and code

1. Client Page
![image](https://user-images.githubusercontent.com/14789754/113967078-e3ff5f80-984d-11eb-9b62-2353878fd6b3.png)

2. Authenticator page( notice the parameters like client_id and return_uri in the URL)
![image](https://user-images.githubusercontent.com/14789754/113967146-0abd9600-984e-11eb-9cb0-ba778d470e09.png)

3. Redirecting back to client along with username
![image](https://user-images.githubusercontent.com/14789754/113967317-5ec87a80-984e-11eb-8d42-3d24cc7b1dfc.png)



