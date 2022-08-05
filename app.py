from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

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

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
