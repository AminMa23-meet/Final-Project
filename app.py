from flask import Flask, render_template, request , redirect, url_for, flash
from flask import session as login_session
from py_edamam import PyEdamam
import pyrebase
import requests
import json
from google_trans_new import google_translator



config = {
  "apiKey": "AIzaSyAdcpJcL5MMkxaKYrGzonf0K-4xF0u0EbA",
  "authDomain": "final-project-afec5.firebaseapp.com",
  "projectId": "final-project-afec5",
  "storageBucket": "final-project-afec5.appspot.com",
  "messagingSenderId": "325938810040",
  "appId": "1:325938810040:web:0ec5d580d3689b7b2b384d",
  "measurementId": "G-6EZCBZGET1",
  "databaseURL": "https://final-project-afec5-default-rtdb.europe-west1.firebasedatabase.app"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
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
            
            return redirect(url_for('signin'))
       except:
           error = "authentication failed"
    return render_template("signup.html")







@app.route('/home', methods = ['GET','POST'])
def home():
  if request.method == 'POST':
    translator = google_translator()
    search = request.form['lib-search']
    url = "https://recipesapi2.p.rapidapi.com/recipes/" + search
    querystring = {"maxRecipes":"10"}
    headers = {
      "X-RapidAPI-Key": "2b11651568msh9571703c4f17240p1143bdjsne194a2b10d31",
      "X-RapidAPI-Host": "recipesapi2.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    loaded = json.loads(response.text)
    leng = len(loaded['data'])
    return render_template('index.html',loaded = loaded, leng = leng, translator = translator)
  return render_template('index1.html')

if __name__ == '__main__':
  app.run(debug=True)
