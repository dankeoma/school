# DANKEUTO SCHOOL API
The API is developed with flask python as a web package and MySQL databaseand is utilized keying in the required route to aheve the desired aim.

This API is developed for higher istitutions for the smooth running of the school. It covers all the facets of the school. Below are the list of the covered areas:
1. Programs run by the school
2. Faculties 
3. Departments
4. Students
4. Courses
3. Staffs

First at the top of the API is the managing board of the school which comprises:
* The Vice Chancellor
* The Lector
* The Registory
* The Bosary
* Etc

The highest in the heirachy is the VC or te lector who now recruits other members.

The group of people mentioned above are responsible for recruiting staff into the working force of the University. The staff now has the responsiblities of registering students while students register courses. 
The API uses MySQL for its database management. It comprises of many tables:
* The Board table - Comprising of board of directors.
* The staff table - Comprising of the staff
* The student table - Comprising the students record
* The program tables - Comprising of programmes run by the school
* The faculty table - Comprising of faculties
* The department tables - Comprising of departments
* The course table - Comprising of the courses
* etc

# Documentation for the use of the school API 

First the API require a API Key to function. The API key is an authorization by the API developer to the user. The key is required for different routes comprised by the API to function. 

# Documentation for the set up of the school API with database
## Here are the list of the required files as provided
1. app.py
2. error.log
3. .env
1. .gitignore
4. readme.md
5. requirements.txt
6. school.sql

## Setting up the system for the API
### Installing Python, seeting up folder and copying files
* Ensure that python is installed in the sysyem - you can get latest python from [Here](https://www.python.org/downloads/) Download and install python in the system. Type python in command window to display double cussor as shown in figure below to ensure correct installation of python
  ![python interface](https://github.com/user-attachments/assets/9b474ec6-ebac-46ec-837c-b8038a7269aa)


* Create a folder in C drive , you can name it Project or School or any other name. Paste the required files provided.
* Create a virtual environment for the project in the folder by typing the command below in the command window. Make sure you navigate to the folder before typing in the code:
    `C:\Projects> python -m venv venv`
* Activate the the virtual environment using the command:
    ` C:\Projects> .venv\Scripts\Activate`

It wil now show: 

(venv)C:\Projects>
* Install the required packages in the virtual environment container using the  command below:

`C:\Projects>pip install -r requirements.txt`

 Note the packages are provided in the requirements.txt
    
* After the istallation you can type the command:
    `C:\Projects>pip freeze` 

to see the installed packages as shown below;
![pip freeze](https://github.com/user-attachments/assets/0395ee96-69f3-4924-b32a-4f6778945c10)


### Installing MYSQL shell and workbench and setting up the database
* Ensure that [MYSQL](https://www.mysql.com/downloads/ "Click to download MYSQL") is installed in the system. Click The link to download mysql workbench and shell. Open command window and type `mysqlsh` to display the figure below to ensure that Mysql is working correctly
  ![mysqltest](https://github.com/user-attachments/assets/888170bd-cf51-4f31-8e66-240f8cff0851)

* After installing MYSQL, open the workbench and create a database called school. You can learn to create database in MySQL workbench [Here](https://stackoverflow.com/questions/5515745/create-a-new-database-with-mysql-workbench "Create database in MySQL Workbench").
Open the command window and put the below command to copy the database package provided into the already created database in workbench, where you will be prompted to inpute your password as shown in the figure:
    `C:\Project> mysqldump -u root -p school < school.sql`
![mysqlprompt](https://github.com/user-attachments/assets/332b8cd7-1aec-48eb-8e23-46bf0d988304)

NOTE! Ensure that the path to Python   `C:\Users\hp\AppData\Local\Programs\Python\Python39\`and  MYSQL server bin `(C:\Program Files\MySQL\MySQL Server 8.0\bin)` is copied to the system's environmental variable. You can learn about that [here](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Environment_Variables.html). 
## Testing The API with Postman
