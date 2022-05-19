#we need access to our Flask object
from app import app

#route deocrator will go by the following syntax:
# @<flask object/blueprint name>.route('/url endpoint', <methods>)

@app.route('/')
def home():
    greeting = 'Hello, Foxes!'
    print(greeting)
    return 'Hello, world.'

