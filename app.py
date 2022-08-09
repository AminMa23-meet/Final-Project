from flask import Flask, render_template, redirect, url_for, flash
from flask import session as login_session
from py_edamam import PyEdamam
import pyrebase
import requests
import json

config = {
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









@app.route('/')
def home():
  url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"
  querystring = {"ingr":"apple"}
  headers = {
    "X-RapidAPI-Key": "2b11651568msh9571703c4f17240p1143bdjsne194a2b10d31",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  loaded = json.loads(response.text)
  return render_template('index.html',loaded = loaded)



if __name__ == '__main__':
  app.run(debug=True)