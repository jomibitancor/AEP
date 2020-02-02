import os
import jwt
import datetime
from aep import app
from flask import jsonify, request
from functools import wraps
from aep.database import Database

app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') 
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return {'message': 'Token is missing or invalid'}

        return f(*args, **kwargs)

    return decorated

@app.route("/")
def main_():
    return "<h1>o!<h1>"

@app.route("/protected")
@token_required
def protected():
    return "Lmao gottem!"

@app.route("/login", methods= ['POST'])
def login():
    
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    db = Database()
        
    if db.verify(username, password):
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return {"token": token.decode('UTF-8')} 
    else:
        return {"message": "Login failed! Please check your credentials"}

    # except:
    #     return {"message": "ERROR: Unauthorized"}
