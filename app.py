from flask import Flask, request, jsonify, session
import logging
import mysql.connector
import datetime
from dateutil.relativedelta import relativedelta
import decimal
import jwt
from functools import wraps
import json
import bcrypt
import secrets
import string
import requests
import os
from dotenv import load_dotenv, dotenv_values
from flask_bcrypt import Bcrypt

load_dotenv()
#....................................................................
#Set global limit and offset
limit1 = 5
offset1 = 0

#.....................................................................
#Generate API Key
def gnrApi():
  from keycove import generate_token, hash
  apiKey = generate_token()
  return hash(value_to_hash=apiKey)

#....................................................................
#Hash password using Bcrypt

def hash_password(password): 
   password_bytes = password.encode('utf-8')
   hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
   return hashed_bytes.decode('utf-8')
#......................................................................
#Create functions to generate student codes(Reg.No)

def student_code():
    characters = string.digits
    code = ''.join(secrets.choice(characters) for _ in range(10))
    sql ='select 1 from student where regno = %s'
    my_cursor.execute(sql,("STD-"+ code,))
    dat = my_cursor.fetchall()
    if dat == []:
      return "STD-"+ code
    else:
      return student_code()
#.........................................................................
#Create functions to generate staff codes(Staff.No)
def staff_code():
    characters = string.digits
    code = ''.join(secrets.choice(characters) for _ in range(4))
    sql ='select 1 from staff where staffNo = %s'
    my_cursor.execute(sql,("STF-"+ code,))
    dat = my_cursor.fetchall()
    if dat == []:
      return "STF-"+ code
    else:
      return staff_code()
    
#.........................................................................
#Generate depaartment code
def getDeptCode():
  code1 = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(2))
  code2 = ''.join(secrets.choice(string.digits) for _ in range(2))
  code = code2+code1
  
  #Check whether department code already exist
  sql ='select 1 from department where deptCode = %s'
  my_cursor.execute(sql,(code,))
  dat = my_cursor.fetchall()
  if dat == []:
    return code
  else:
    return getDeptCode()
#...........................................................................  
#Send Email 
def send_email(to,subject,text):
  from mailjet_rest import Client
  api_key = os.getenv("mailjet_Api")
  api_secret = os.getenv("mailjet_secret_key")
  mailjet = Client(auth=(api_key, api_secret), version='v3.1')
  data = {
    'Messages': [
      {
        "From": {
          "Email": os.getenv("email_sender_email"),
          "Name": os.getenv("email_sender_name")
        },
        "To": to, #list of objects
        "Subject": subject,#string
        "TextPart": text,#string
        "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        "CustomID": "AppGettingStartedTest"
      }
    ]
  }
  result = mailjet.send.create(data=data)
  print (result.status_code)
  print (result.json())
#.........................................................................
#Send SMS
def send_sms(to,body):
  
  url = "https://www.bulksmsnigeria.com/api/v1/sms/create"
  params = {
    "api_token": os.getenv("sms_app_token"),
    "from":os.getenv("sms_sender_name"),
    "to":to,
    "body":body
  }
  resp = requests.post(url, data=params)
  print(resp.json()) 

#........................................................................
#Take care of date time and decimal
def default(o):
  if type(o) is datetime.date or type(o) is datetime.datetime:
    return o.isoformat()
  if type(o) is decimal.Decimal:
    return float(o)
  
#.......................................................................
#log in information to the error.log
logging.basicConfig(filename='error.log',level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)
#.........................................................................
# Configuration
app.config['SECRET_KEY'] = os.getenv("app_secrete_key")
#.......................................................................
#Connection to Mysql database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "DANKEsweet287",
  database = os.environ.get("mysqli_database")
)
my_cursor = mydb.cursor()
#.........................................................................
#Generate vendocode

def vendocode():
    characters = string.digits
    code = ''.join(secrets.choice(characters) for _ in range(10))
    sql ='select 1 from params where vendorCode = %s'
    my_cursor.execute(sql,(code,))
    dat = my_cursor.fetchall()
    if dat == []:
      return code
    else:
      return vendocode() 

#.......................................................................
#Check the login token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      
        headers = request.headers
        bearer = headers.get('Authorization')    # Bearer YourTokenHere
        print(bearer)
        token = bearer.split()[1]  # YourTokenHere
        # token = request.args.get()
        # data = request.get_json()
        # token = data['token']
        print(token)
        if not token:
            return jsonify({'error': 'token is missing'}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'] , "HS256")
        except Exception as error:
            return jsonify({'error': 'token is invalid/expired'}),403
        return f(*args, **kwargs)
    return decorated 
  
#......................................................................   
#Check the API Key
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
      try:
        if request.headers.get('apiKey') and request.headers.get('vendorCode'):
          vendorCode = request.headers.get('vendorCode')
          currentDate = datetime.date.today()
          #Connect the params table
          sql1 = 'select apiKey,expiresAt from params where vendorCode = %s'
          value = (vendorCode,)
          my_cursor.execute(sql1,value)
          dat1 = my_cursor.fetchall()
          if dat1 == []:
            return jsonify({"Error": "vendorCode not in database"}),403
          print(dat1[0][1],currentDate) 
          if request.headers.get('apiKey') == dat1[0][0] and currentDate < dat1[0][1]:
            return view_function(*args, **kwargs)
          else:
              return jsonify({'Error': 'Incorrect apiKey'}),403
        else:
          return jsonify({"Error":"apiKey and or vendorCode required or expired"}),403
      except Exception:
        return jsonify({"Error": "Something went wrong, Api key configuration"})
    return decorated_function
#........................................................................
# ROUTES
#............................................................................
#Home
@app.route('/', methods = ["POST"])
def get_api_key():
  try:
    data = request.get_json()
    if 'payment' in data and isinstance(data['payment'],str) and data['payment'].lower()== 'confirm':
      if 'vendor' in data and 'director' in data:
        if isinstance(data["vendor"],str) and isinstance(data["director"],str):
          vendor = data["vendor"]
          director = data["director"]
          
          vendo_code = vendocode()
          
          api_key = gnrApi()
          print(api_key)
          createdDate = datetime.date.today()
          expireDate = createdDate + relativedelta(months=3)
          db = "school"
          print(expireDate)
          #Insert into the param table
          try:
            sql = 'insert into params (apiKey,vendorCode,vendor,createdAt,expiresAt,db,director)\
            values(%s,%s,%s,%s,%s,%s,%s)'
            values = (api_key,vendo_code,vendor,createdDate,expireDate,db,director)
            my_cursor.execute(sql,values)
            mydb.commit()
            app.logger.info("Done: API Key generated successfully")
            return jsonify({"Data":{
            "ApiKey": api_key,
            "vendorCode": vendo_code,
            "Expire Date": expireDate},
                          "Status": "Success",
                          "Code":"00",
                          "Message":"Api Key generated successfully"})
          except Exception:
            app.logger.error("Error: Cant save into params table. Check databse connection")
            return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Incorrect data type for vendor and or director"})
            
        else:
          app.logger.error("Error: Incorrect data type for vendor and or director")
          return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Incorrect data type for vendor and or director"})
      else:
        app.logger.error("Error: Request body must contain vendor and director")
        return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"Request body must contain vendor and director"})
    else:
      app.logger.error("Error: payment required in the request body")
      return jsonify({"Data":None,
                          "Status": "Failed",
                          "Code":"01",
                          "Message":"payment required in the request body "})
  except Exception:
    app.logger.error("Error: Something went wrong, missing or wrong request body")
    return jsonify({"Data":None,
                        "Status": "Failed",
                        "Code":"01",
                        "Message":"Something went wrong, missing or wrong request body"})
    
@app.route('/home')
@require_appkey
def home():
  return '<h1>Hi I am Daniel, Hello World!!</h1>'
#........................................................................
#FACULTY
#.......................................................................
#select all Faculties in the school
@app.route('/faculty/list/all', methods=["POST"])
@require_appkey
@token_required
def faculty_all():
  try:
    #get the request body
    data = request.get_json()
  
    #Make sure limit and offset is contained in request body
    if 'limit' in data and 'offset' in data:
      limit = data['limit']
      offset = data['offset']
      #Make sure limit and offset PARAM are of integer data type
      if isinstance(limit,int) and isinstance(offset,int):
        #Make sure limit doesnt exceed supposed
        if limit > 10:
          limit = limit1 
        sql = 'select * from faculty limit %s offset %s'
        my_cursor.execute(sql,(limit,offset))
        dat = my_cursor.fetchall()
        app.logger.info("Done: Data retrieved successfully")
        return jsonify({"data":dat,
                          "status":"Sucess",
                          "message":"Data retrieved successfully",
                          "code":"00"})
      else:
        app.logger.error("Value type integer expected from key limit")
        return jsonify({"data":"None",
                            "status":"Failed",
                            "message":"Value type integer expected from key limit and offset",
                            "code":"01"})
    else:
      app.logger.error("PARAM must contain limit and offset key")
      return jsonify({"data":"None",
                          "status":"Failed",
                          "message":"Request body must contain limit and offset key PARAM",
                          "code":"01"})
  except:
    app.logger.error("Call must contain a JSON request body")
    return jsonify({"data":"None",
                        "status":"Failed",
                        "message":"Call must contain a JSON request body",
                        "code":"01"})
#........................................................................
#Search for faculty
@app.route('/faculty/search', methods=['POST'])
@require_appkey
@token_required
def faculty_search():
  try:
    data = request.get_json()
    lim = limit1
    off = offset1
    if 'search' in data:
      search= data['search']
      if 'limit' in data and isinstance(data['limit'],int):
        limit = data['limit']
        if limit < lim:
          lim = limit
        else:
            pass
      if 'offset' in data and isinstance(data['offset'],int):
        offset = data['offset']
        if offset > off:
          off = offset
               
      sql = 'select * from faculty where\
           facName like %s\
        or facDean like %s\
          limit %s offset %s'
      my_cursor.execute(sql,('%'+search+'%','%'+search+'%',lim,off))
      dat = my_cursor.fetchall()
      app.logger.info("Done: Data retrieved successfully")
      return jsonify({"data":dat,
                        "status":"Sucess",
                        "message":"Data retrieved successfully",
                        "code":"00"})
    else:
      app.logger.error("Error: Search Param not in request body")
      return jsonify({"data":None,
                        "status":"Failed",
                        "message":"Search Param not in request body",
                        "code":"01"})
  except Exception:
    app.logger.error("Error: Something whent wrong with the code! OR the request body not JSON")
    return jsonify({"data":None,
                        "status":"Failed",
                        "message":"Something whent wrong with the code! OR the request body not JSON",
                        "code":"01"})
#........................................................................
#Get particular faculty by faculty id
@app.route('/faculty/list/one/',methods=['POST'])
@require_appkey
@token_required
def faculty_one():
  try:
    data = request.get_json()
    if 'id' in data and isinstance(data['id'],int):
      id = data['id']
      sql = 'select * from faculty where facID = %s'
      my_cursor.execute(sql,(id,))
      dat = my_cursor.fetchall()
      app.logger.info("Done: Data retrieved successfully")
      return jsonify({"data":dat,
                        "status":"Sucess",
                        "message":"Data retrieved successfully",
                        "code":"00"})
    else:
      app.logger.error("Error: Id of integer data type not contained in the request body")
      return jsonify({"data":None,
                        "status":"Failed",
                        "message":" Id of integer data type not contained in the request body",
                        "code":"01"})

  except Exception:
      app.logger.error("Error: Syntax error from  either the code or request body")
      return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Error: Syntax error from  either the code or request body",
                        "code":"01"})
#........................................................................
#Register a staff 
@app.route('/register-staff', methods=['POST'])
@require_appkey
@token_required
def register_staff():
  try:
    data = request.get_json()
    if all(key in data for key in('staffName','staffEmail','staffPhone','password')):
      if isinstance(data['staffName'],str) and isinstance(data['staffEmail'],str)\
        and isinstance(data['staffPhone'],str) and isinstance(data['password'],str):
          
        staffName = data['staffName']
        staffEmail = data['staffEmail']
        staffPhone = data['staffPhone']
        password = data['password']
        
        #Get staff number/code
        staffNo = staff_code()
        
        #Harsh the password
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt()
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        
        #Create staff record
        sql = 'insert into staff(staffName,staffNo,staffEmail,staffPhone,password) values(%s,%s,%s,%s,%s)'
        values =(staffName,staffNo,staffEmail,staffPhone,hashed_pw)
        my_cursor.execute(sql,values)
        mydb.commit()
        
        app.logger.info("Done: Staff data created  successfully")
        return jsonify({"Data":{"StaffNo.": staffNo,},
                          "Status":"Sucess",
                          "Message":"Staff data created successfully",
                          "Code":"00"})
      else:
        app.logger.error("Error: Check the data type of the PARAMs in the request body")
        return jsonify({"Data": None,
                          "Status":"Failed",
                          "Message":"Check the data type of the PARAMs in the request body",
                          "Code":"01"})
    else:
      app.logger.error("Error: Incomperete PARAM in request body(stf_name,stf_email,stf_phone)")
      return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Incomperete PARAM in request body(stf_name,stf_email,stf_phone)",
                        "code":"01"})
        
  except Exception:
    app.logger.error("Error: Syntax error from  either the code or request body")
    return jsonify({"Data":None ,
                      "status":"Failed",
                      "message":"Error: Syntax error from  either the code or request body",
                      "code":"01"})
#........................................................................
#Register student 
@app.route('/register/',methods=['POST'])
@require_appkey
@token_required
def register():
  headers = request.headers
  bearer = headers.get('Authorization')    # Bearer YourTokenHere
  token = bearer.split()[1]
  data=jwt.decode(token, app.config['SECRET_KEY'] , "HS256")
  isStaff = data['isStaff']
  staffID = data['staffID']
  if not(isStaff == 1 and staffID is not None):
    app.logger.error("Error: You most be logged in as a staff")
    return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"You most be logged in as a staff",
                        "code":"01"})
  
  try:
    data = request.get_json()
    if 'user' in data and isinstance(data['user'],str):
      user = data['user']
      if (user.replace(" ","")).lower() == "student":
        if all(key in data for key in('fullName','phone','age','state','deptName','password','email','regYear')):
          if isinstance(data['fullName'],str) and isinstance(data['phone'],str) and isinstance(data['age'],int)\
            and isinstance(data['state'],str)and isinstance(data['deptName'],str)\
              and isinstance(data['password'],str)and isinstance(data['email'],str)and isinstance(data['regYear'],int):
              
    
            fullName = data['fullName']
            phone = data['phone'].replace(" ","")
            age = data['age']
            state = data['state']
            deptName = data['deptName']
            password = data['password'].replace(" ","")
            email = data['email'].replace(" ","")
            regYear = data['regYear']
            
            # Get the id of the department
            sql = 'select deptID from department where deptName = %s'
            value = (deptName,)
            my_cursor.execute(sql,value)
            deptDat = my_cursor.fetchall()
            if deptDat == []:
              return jsonify({"Error": "Department name not existing. Check for correct spelling and spacing"})
            deptID = deptDat[0][0]
            
            
            #Harsh the password
            from flask_bcrypt import Bcrypt
            bcrypt = Bcrypt()
            hashe_pw = bcrypt.generate_password_hash(password).decode('utf-8')
            
            # Get the count of student in database and add one
            sql = 'select count(regYear) from deptstudent where regYear = %s'
            value = (regYear,)
            my_cursor.execute(sql,value)
            dat = my_cursor.fetchall()
            last_stuNo = dat[0][0]
            next_stuNo = last_stuNo + 1
            stuNo = str(next_stuNo).zfill(5)
            
            #Get current time
            createdTime = datetime.date.today()
            
            
            #Create student record
            sql = 'insert into student(fullName,phone,age,state,password,email,createdBy,createdAt) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            values =(fullName,phone,age,state,hashe_pw,email,staffID,createdTime)
            my_cursor.execute(sql,values)
            mydb.commit()
            
            #Get student id
            sql = 'select stuID from student where fullName = %s'
            value = (fullName,)
            my_cursor.execute(sql,value)
            stuDat = my_cursor.fetchall()
            stuID = stuDat[0][0]
            
            
            #Create deptstudent data
            sql = 'insert into deptstudent(stuID,deptID,regYear,stuNo) values(%s,%s,%s,%s)'
            values =(stuID,deptID,regYear,stuNo)
            my_cursor.execute(sql,values)
            mydb.commit()
            
            #Send SMS
            try:
              to = phone
              text = "student data created successfull and the student number is {}".format(stuNo)
              send_sms(to,text)
            except Exception:
              return jsonify({"Error":"Error sending SMS"})
            
            #Send Email
            try:
              to = email
              subject = "Student Data Created"
              text = "student data has beencreated successfull and the student number is {}".format(stuNo)
              send_email(to,subject,text)
            except Exception:
              return jsonify({"Error":"Error sending Email"})
            
            #Log out values on success
            app.logger.info("Done: Student/DeptStudent data created successfully")
            return jsonify({"Data":{"studentName":fullName,
                            "studentNo":stuNo,
                            "regNo": "No regNo yet"},
                              "Status":"Sucess",
                              "Message":"Student/DeptStudent data created successfully",
                              "Code":"00"})
            
          else:
            app.logger.error("Error: Check the data type of the PARAMs in the request body")
            return jsonify({"data": None,
                              "status":"Failed",
                              "message":"Check the data type of the PARAMs in the request body",
                              "code":"01"})
        else:
          app.logger.error("Error: Incomperete PARAM in request body(fullname,phone,age,state,deptName,password,email,regYear)")
          return jsonify({"Data":None ,
                            "status":"Failed",
                            "message":"Incomperete PARAM in request body(fullname,phone,age,state,deptName,password,email,regYear)",
                            "code":"01"})
          
      
  except Exception:
    app.logger.error("Error:You may be trying to double register a candidate with Phone number or Email that has been used before")
    return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":" You may be trying to double register a candidate with Phone number or Email that has been used before",
                        "code":"01"})
#......................................................................
#Login as a Student using regNo or as a staff using staffNo  
@app.route('/login/',methods=['POST'])
@require_appkey
def login():
  try:
    data = request.get_json()
    if all(key in data for key in('userid','password')):
      if isinstance(data['userid'],str) and isinstance(data['password'],str):
        userid = data['userid']
        password = data['password']
        
        bcrypt = Bcrypt()
        
        
        #Check if the user is a student
        sql1 ='select 1 from student where regNo= trim(%s)'
        my_cursor.execute(sql1,(userid,))
        dt = my_cursor.fetchall()
        
        if dt != []:
          sql2 = 'select password from student where regNo = trim(%s)'
          my_cursor.execute(sql2,(userid,))
          dt1=my_cursor.fetchall()
          dt2=dt1[0][0]
      
          #compare the passwords
          if bcrypt.check_password_hash(dt2,password) == True:
            sql3 = 'select stuID,fullName from student where regNo=trim(%s)'
            my_cursor.execute(sql3,(userid,))
            dt3 = my_cursor.fetchall()
            print(dt3)
            session['logged_in'] = True
            token = jwt.encode({
            'isStudent':1,
            'isStaff':0,
            'stuID': dt3[0][0],
            'staffID': None,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=50)}, app.config['SECRET_KEY'])
            
            #Add the logs to the api_logs table in the database
            studentID = dt3[0][0]
            studentName = dt3[0][1]
            req_data ={"StudentID": studentID,"studentName":studentName}
            res_data ={"UserID": userid,"Password":password}
            sql = 'insert into api_logs(IP,request,response,route) values(%s,%s,%s,%s)'
            values = (request.remote_addr,json.dumps(res_data),json.dumps(req_data),request.path)
            my_cursor.execute(sql,values)
            mydb.commit()
            
            app.logger.info("Done: Signed in as Student")
            return jsonify({"Data":{"Name":dt3[0][1],
                              "token":token},
                              "status":"Success",
                              "message":"Signed in as Student",
                              "code":"00"})
          else:
            app.logger.error("Error: Wrong password please check the password")
            return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Wrong password please check the password",
                       "code":"01"})
        else:
          #Check if the user is a staff
          sql3 ='select 1 from staff where staffNo=trim(%s)'
          my_cursor.execute(sql3,(userid,))
          dt1 = my_cursor.fetchall()
          if dt1 != []:
            sql4 = 'select password from staff where staffNo = trim(%s)'
            my_cursor.execute(sql4,(userid,))
            dt3=my_cursor.fetchall()
            dt4=dt3[0][0]
        
            #compare the passwords
            if bcrypt.check_password_hash(dt4,password) == True:
              sql5 = 'select staffid,staffName,staffNo from staff where staffNo=trim(%s)'
              my_cursor.execute(sql5,(userid,))
              dt5 = my_cursor.fetchall()
              session['logged_in'] = True
              token = jwt.encode({
             'isStudent':0,
             'isStaff':1,
             'stuID': None,
             'staffID': dt5[0][0],
             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=50)}, app.config['SECRET_KEY'])
              #Add the logs to the api_logs table in the database
              staffID = dt5[0][0]
              staffName = dt5[0][1]
              req_data ={"StaffID": staffID,"staffName":staffName}
              res_data ={"UserID": userid,"Password":password}
              sql = 'insert into api_logs(IP,request,response,route) values(%s,%s,%s,%s)'
              values = (request.remote_addr,json.dumps(res_data),json.dumps(req_data),request.path)
              my_cursor.execute(sql,values)
              mydb.commit()
              
              app.logger.info("Done: Signed in as Staff")
              return jsonify({"Data":{"staffID":dt5[0][0],
                              "staffName": dt5[0][1],
                              "token":token},
                              "Status":"Success",
                              "Message":"Signed in as Staff",
                              "Code":"00"})
            else:
              app.logger.error("Error: Wrong password please check the password")
              return jsonify({"Data":None ,
                          "status":"Failed",
                          "message":"Wrong password please check the password",
                          "code":"01"})
          else:
            app.logger.error("Error: Not a student nor a staff UserID not in database")
            return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Not a student nor a staff UserID not in database",
                        "code":"01"})
      else:
        app.logger.error("Error: Check data type of the PARAM in the request body(userid and password)")
        return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Error: Check data type of the PARAM in the request body(userid and password)",
                        "code":"01"})
    else:
      app.logger.error("Error: Incomplet PARAM in request body(userid and password)")
      return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Error: Incomplet PARAM in request body(userid and password)",
                        "code":"01"})
  except Exception:
    app.logger.error("Error: Syntax error from  either the code or request body")
    return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Error: Syntax error from  either the code or request body",
                        "code":"01"})

    
#Generate Student regNo
@app.route('/generate_regNo', methods=['POST'])
@require_appkey
@token_required
def generate_regno():
  headers = request.headers
  bearer = headers.get('Authorization')    # Bearer YourTokenHere
  token = bearer.split()[1]
  data=jwt.decode(token, app.config['SECRET_KEY'] , "HS256")
 
  isStaff = data['isStaff']
  staffID = data['staffID']
  if not(isStaff == 1 and staffID is not None):
    app.logger.error("Error: You most be logged in as a staff")
    return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"You most be logged in as a staff",
                        "code":"01"})
  try:
    data = request.get_json()
    if 'stuID' in data and isinstance(data['stuID'],int):
      stuID = data['stuID']
      sql = 'select 1 from student where stuID = %s'
      my_cursor.execute(sql,(stuID,))
      dat = my_cursor.fetchall()
      
      if dat == []:
        app.logger.error("Error: No matching identity, student not in record")
        return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"No matching identity, student not in record",
                        "code":"01"})
      
      sql = 'select regNo from student where stuID = %s and length(regNo)>=10 and regNo is not null and regNoGenerated=1'
      value = (stuID,)
      my_cursor.execute(sql,value)
      dat = my_cursor.fetchall()
      if dat !=[]:
         app.logger.info("Message: Student already has Registration Number")
         return jsonify({"Data":{"regNo": dat[0][0],
                        },
                        "Status":" Failed",
                        "Code":'01',
                        "Message":"Student already has Registeration Number"})
         
      #Get department number
      dept_sql = 'select deptCode from department where deptID = (select deptID from deptstudent where stuID=%s)'
      my_cursor.execute(dept_sql,(stuID,))
      dept_dat = my_cursor.fetchall()
      
      
      #Get student number and admission year
      stu_sql = 'select deptstudent.stuNo, deptstudent.regYear,student.fullName from deptstudent inner join student on deptstudent.stuID=student.stuID where deptstudent.stuID = %s'
      my_cursor.execute(stu_sql,(stuID,))
      stu_dat = my_cursor.fetchall()
     
      #Combine to get the registeration Number
      regNo = str(stu_dat[0][1]) + dept_dat[0][0] + stu_dat[0][0]
  
      genDate = datetime.date.today()
      
      
      #Save registeration number in the students table
      dept_sql = 'update student set regNo = %s,regNoGenerated=%s,regNoGeneratedBy=%s,regNoGeneratedAt=%s where stuID=%s'
      my_cursor.execute(dept_sql,(regNo,1,staffID,genDate,stuID))
      mydb.commit()
      
      app.logger.info("Message: Student Registeration number successfully generated")
      return jsonify({"Data":{"regNo": regNo,
                        "StudentName":stu_dat[0][2],
                        "studentNo": stu_dat[0][0]},
                      "Code":"00",
                      "Message":"Student Registeration number successfully generated",
                      "Status":"Success"
                        })
      
    else:
      app.logger.error("Error: Param must contain search of string data type")
      return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"Param must contain search of string data type",
                        "code":"01"})
  except Exception:
    app.logger.error("Error: Syntax error from  either the code or request body")
    return jsonify({"Data":None ,
                        "status":"FAiled",
                        "message":"Error: Syntax error from  either the code or request body",
                        "code":"01"})
    
#Create department
@app.route('/department/insert', methods=['POST'])
@token_required
def department_insert():
  headers = request.headers
  bearer = headers.get('Authorization')    # Bearer YourTokenHere
  token = bearer.split()[1]
  data=jwt.decode(token, app.config['SECRET_KEY'] , "HS256")
  print (data)
  isStaff = data['isStaff']
  staffID = data['staffID']
  if not(isStaff == 1 and staffID is not None):
    app.logger.error("Error: You most be logged in as a staff")
    return jsonify({"Data":None ,
                        "status":"Failed",
                        "message":"You most be logged in as a staff",
                        "code":"01"}) 
  
  try:
    data = request.get_json()
    if all(key in data for key in('deptName','deptAbrv','facID')):
      if isinstance(data['deptName'],str) and isinstance(data['deptAbrv'],str)and isinstance(data['facID'],int):
        deptName = data['deptName']
        deptAbrv = data['deptAbrv']
        facID = data['facID']
        deptCode = getDeptCode()
        createdDate=datetime.date.today()
        
        sql = 'insert into department(deptName,deptAbrv,facID,deptCode,createdBy,createdAt) values(%s,%s,%s,%s,%s,%s)'
        values = (deptName,deptAbrv,facID,deptCode,staffID,createdDate)
        my_cursor.execute(sql,values)
        mydb.commit()
        
        app.logger.info("Info: Department inserted successfully")
        return jsonify({"Data":None ,
                        "status":"success",
                        "message":"Department inserted successfully",
                        "code":"00"})
        
      else:
        app.logger.error("Error: deptName and deptAbrv must be of string data type while facID if of integer type")
        return jsonify({"Data":None ,
                        "status":"FAiled",
                        "message":"deptName and deptAbrv must be of string data type while facID if of integer type",
                        "code":"01"})
    else:
      app.logger.error("Error: The request body must contain deptName, deptAbrv and facID")
      return jsonify({"Data":None ,
                        "status":"FAiled",
                        "message":"The request body must contain deptName and deptAbrv and facID",
                        "code":"01"})
  except Exception:
    app.logger.error("Error: Syntax error from  either the code or request body")
    return jsonify({"Data":None ,
                      "status":"FAiled",
                      "message":"Error: Syntax error from  either the code or request body",
                      "code":"01"})




if __name__ == '__main__':
    app.run(debug=True)