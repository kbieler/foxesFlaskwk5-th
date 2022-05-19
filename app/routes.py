#we need access to our Flask object
from app import app

from flask import render_template 

import requests as r

#route deocrator will go by the following syntax:
# @<flask object/blueprint name>.route('/url endpoint', <methods>)

@app.route('/')
def home():
    greeting = 'Welcome to Flask week, Foxes!'
    print(greeting)
    return render_template('index.html', g=greeting) 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/players')
def players():
    #make an API call and utilize info from that PI call in teh HTML templating
    data = r.get('https://foxes90-prempundit.herokuapp.com/players')
    if data.status_code == 200:
        data = data.json()
    return render_template('players.html', data = data)