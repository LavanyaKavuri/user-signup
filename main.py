from flask import Flask , request , redirect , render_template
import random , re
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")

def index():
   
    
    template = jinja_env.get_template('index.html')
    return template.render()

def isEmp(str): 
    if len(str) == 0: 
        return 0
    else: 
        return 1
   
def isalpha(str):
    if re.match(r'^\w+$', str):
        return 0
    else:
        return 1    
def emailalpha(str) :
    if str == '@' or str == '.' or str== ' ':
        return 0
    else:
        return 1 


@app.route("/user_signup", methods=['POST'])

def name1():
    # choose a movie by invoking our new function
   user = request.form['user']
   pwd= request.form['pwd']
   cpwd=request.form['cpwd']
   email= request.form['email']
   email_error=''
   user_error = ''
   pwd_error = ''
   cpwd_error= ''
   
   if  not isEmp(user) :
       user_error ="The username is Empty"
   else:
       if len(user) >20 or len(user) < 3 or  isalpha(user):
           user_error ="The username should be in between 3 to 20"
   if  not isEmp(pwd) :
       pwd_error ="The password is Empty"
   else:
       if len(pwd) > 20 or len(pwd) < 3 or  isalpha(pwd):
          pwd_error ="The password should be in between 3 to 20" 

   if  cpwd != pwd or not isEmp(cpwd):
       cpwd_error= "The password and the confirm password did not match"
   if   emailalpha(email) or len(email) > 20 or len(email) < 3:
       email_error ="Please enter a valid email"
   if not   email_error and not  user_error and not  pwd_error and not  cpwd_error:
       return render_template('final_output.html', user=user)
   else: 
       template = jinja_env.get_template('index.html')
       return  template.render(user=user,user_error=user_error,pwd_error=pwd_error,cpwd_error=cpwd_error,email=email,email_error=email_error)





app.run()
