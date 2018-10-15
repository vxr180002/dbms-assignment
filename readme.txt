ReadMe
Source code: https://github.com/vxr180002/dbms-assignment.git 
This document contains 
1. Description of tools/technologies used in this project
2. How to compile, build and install this application

Description of tools/technologies use in this project:
a. Languages used: Python, HTML
b. Web Framework: Django
c. Database: SQLITE3
d. Dependencies: All library dependencies are laid out in requirements.txt file. 
How to compile, build and install this application:
a. Install Python 3.6 and pip3 for python
b. Clone repo using “$ git clone https://github.com/vxr180002/dbms-assignment.git”
c. $ cd dbms-assignment
d. $ pip3 install virtualenv
e. $ virtualenv my_project
f. now to activate the virtual environment “$ source my_project_bin_activate”
g. now the virtual env is active.
h. Install all dependencies of the project using “$ pip3 install -r requirements.txt”
i. To make changes to the model and underlying database use
1. $ python manage.py makemigrations
2. $ python manage.py migrate
j. “$ python manage.py runserver” to run the application on localhost:8000
k. Go to url: http://127.0.0.1/8000/polls to go to the homepage of the GUI application.


      The End 
