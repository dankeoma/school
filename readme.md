# DANKEUTO SCHOOL API
This API is developed for higher istitutions for the smooth running of the school. It covers all the facets of the school. Below are the list of the covered areas:
1. Programs run by the school
2. Faculties 
3. Departments
4. Students
4. Courses
3. Staffs


# Documentation for the set up of the school API with database
## Here are the list of the required files as provided
1. app.py
2. error.log
3. keys.py
4. readme.md
5. requirements.txt
6. school.sql

## Setting up the system for the API
### Installing Python, seeting up folder and copying files
* Ensure that python is installed in the sysyem - you can get latest python from [Here](https://www.python.org/downloads/) Download and install python in the system

* Create a folder in C drive , you can name it Project or School or any other name. Paste the six required files provided.
* Create a virtual environment for the project in the folder by typing the command below in the command window. make sure you vavigate to the folder before typing in the code:
    * C:\Projects> python -m venv venv
* Activate the the virtual environment using the command:
    * C:\Projects> .venv\Scripts\Activate.

It wil now show: (venv)C:\Projects>
* Install the required packages in the virtual environment container using the  command below: Note the packages are provided in the requirements.txt
    * C:\Projects>pip install -r requirements.txt
* After the istallation you can type the command:
    * C:\Projects>pip freeze 

to see the installed packages.
### Installing MYSQL shell and workbench and setting up the database
* Ensure that [MYSQL](https://www.mysql.com/downloads/ "Click to download MYSQL") is installed in the system. Click The link to download mysql workbench and shell.
* After installing MYSQL, open the workbench and create a database called school. You can learn to create database in MySQL workbench [Here](https://stackoverflow.com/questions/5515745/create-a-new-database-with-mysql-workbench "Create database in MySQL Workbench").
Open the command window and put the below command to copy the database package provided into the already created database in workbench, where you will be prompted to inpute your password:
    * C:\Project> mysqldump -u root -p school < school.sql

NOTE! Ensure that the path to the MYSQL server bin (C:\Program Files\MySQL\MySQL Server 8.0\bin) is copied to the system's environmental variable. You can learn about that [here](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html).
## Before Using The API
Open the keys.py package in a code editor like sublime text or visual code editor and change the passwords and keys to match with your keys and passwords especiall the database_password