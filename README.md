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

Some screenshots of the flow and code

1. Client Page
![image](https://user-images.githubusercontent.com/14789754/113967078-e3ff5f80-984d-11eb-9b62-2353878fd6b3.png)

2. Authenticator page( notice the parameters like client_id and return_uri in the URL)
![image](https://user-images.githubusercontent.com/14789754/113967146-0abd9600-984e-11eb-9cb0-ba778d470e09.png)

3. Redirecting back to client along with username
![image](https://user-images.githubusercontent.com/14789754/113967317-5ec87a80-984e-11eb-8d42-3d24cc7b1dfc.png)



