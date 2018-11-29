"""
app root of the api endpoints
"""

from datetime import datetime
import re
from flask import Flask, jsonify, request


APP = Flask(__name__)

# fname = ''
# lname = ''
# users = [{"fname":fname, "lname":lname }]
USERS = [{
    "id": 0,
    "firstName" : "Astone",
    "lastName" : "Tuhame",
    "otherNames" : "Junior",
    "email" : "astonetuhame@gmail.com",
    "phoneNumber" : "0779219779",
    "username" : "Taent",
    "password": "12345",
    "registered":"24/11/2018",
    "isAdmin": False
}]

def _record_exists(email):
    return [user for user in USERS if user["email"] == email]

@APP.route('/api/v1/users', methods=['POST'])
def create_user():
    """Function to create user"""
    if not request.json or 'firstName' not in request.json or 'lastName' not in request.json  or 'otherNames' not in request.json or 'email' not in request.json or 'phoneNumber' not in request.json or 'username' not in request.json  or 'password' not in request.json:
        return jsonify({'error': 'BAD_REQUEST'}), 400
    user_id = USERS[-1].get("id") + 1
    email = request.json.get('email')
    fname = request.json.get('firstName')
    lname = request.json.get('lastName')
    other = request.json.get('otherNames')
    username = request.json.get('username')
    password = request.json.get('password')
    phone = request.json.get('phoneNumber')

    if _record_exists(email):
        return jsonify({'status': 400, 'error':'Email has already been taken'}), 400
    if (type(fname) or type(lname) or type(other) or type(phone) or type(request.json.get(username))) is not str:
        return jsonify({'status': 400, 'error':'Please use character strings'}), 400
    # if not request.json['firstName'] or request.json['lastName'] or request.json['email'] or request.json['phoneNumber'] or request.json['username'] or request.json['password']:
    #     return jsonify({'status': 400,'error':'Please fill in the fields'}), 400
    if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email):
        return jsonify({'status': 400, 'error':'Invalid Email'}), 400
    user = {"id": user_id, "firstName": fname, "lastName": lname, "otherNames": other, "email": email, "phoneNumber": phone, "username": username, "password": password, "registered": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "isAdmin":False}
    USERS.append(user)
    return jsonify({'user': user}), 201




APP.run(debug=True)
