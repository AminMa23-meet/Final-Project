from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import json

Config = {
  "apiKey": "AIzaSyDjObFBsV8oPDN_AXa9cjNPvlKM8QWqisg",
  "authDomain": "final-project-817f0.firebaseapp.com",
  "databaseURL": "https://final-project-817f0-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "final-project-817f0",
  "storageBucket": "final-project-817f0.appspot.com",
  "messagingSenderId": "533293150836",
  "appId": "1:533293150836:web:c35844f392d7972074d721",
  "measurementId": "G-0THL94HBP0" , "databaseURL": "https://final-project-817f0-default-rtdb.europe-west1.firebasedatabase.app/"
};

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       return redirect(url_for('add_tweet'))
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       full_name = request.form['full_name']
       username = request.form['username']
       bio = request.form['bio']

       user = {"full_name": full_name, "username": username,"bio":bio,"email":email,"password":password}
       try:
            login_session['user'] =  auth.create_user_with_email_and_password(email, password)
            db.child("Users").child(login_session['user']['localId']).set(user)
            
            return redirect(url_for('add_tweet'))
       except:
           error = "authentication failed"
    return render_template("signup.html")

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
