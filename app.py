# import                     
from flask import Flask
app = Flask(__name__)

#index route 
@app.route('/')
def index():
    return 'Hello, from PetFax!'   

# pets route 
@app.route('/pets')
def pets():
    return 'Hello, these are our pets available for adoption'