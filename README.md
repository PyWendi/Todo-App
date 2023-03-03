# My Todo App
This is a project which it's main goal is to provide a numeric todo list with user authentication.
This is a simple web-app and easy to use made with Django, a python web framework.
It use a "SQLITE3" database to store data, which is a light and easy to use database.

## Description
This project main goal is to create a private space where you can manage your daily, weekly or monthly planing.
With this app, you can see your tasks, create other tasks, update and even delete tasks.
This app provide a user authentication, which allow the user to see only his/her tasks even if there are multiple user using the app.

## Project setup
_In order to run this project, first of all, you must have python installed on your system.
If you don't have it yet, you can download it in the official website at www.python.org.
_Then use the python package manager [pip](https://pip.pypa.io/en/stable/) to install "django" through the command line using following command:
```
pip install django
```

## Usage
To run the project, go in the directory where the file "manage.py" is located.
Open the command line inside this directory and run the following command to run the project
```
python manage.py runserver
```
After that, there is a warning saying that some migration are not applied.
in the command line, stop the server using "ctrl+C" then type in the terminal the following command:
```
python manage.py makemigrations todo
python manage.py migrate
```
Now run the server again, open your browser and write the open the project on the following URL 
http://127.0.0.1:8000/

Now enjoy

### Manage database and Admin panel
Django provide an admin page where you can manage the app data.
To use it, first create an admin account by typing the following command:
```
python manage.py createsuperuser
```
Then follow the instruction to create the admin account.
After that, run the server and go to the admin page using the following url : http://127.0.0.1:8000/admin/ 
Log into and manage your data :).

### Support 
If there is an issue you want to report about the app or for anything else, contact me using my email address:
rakotondranaivogilbert21@gmail.com
