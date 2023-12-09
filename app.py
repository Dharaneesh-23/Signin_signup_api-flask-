from flask import Flask,request,jsonify
from database import database
from passlib.hash import sha256_crypt
app = Flask(__name__)

@app.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        details = request.json
        required_fields = ['username', 'email', 'password']
        if not all(field in details for field in required_fields):
            return jsonify({'error': 'Missing required fields'})
        username,password = details['username'],details['password']
        hashed_password = sha256_crypt.hash(password)
        str = database(username,hashed_password,'signup',details['email'])
        return jsonify({"response": str})
    elif request.method =='GET':
        return jsonify('signup page')
    
@app.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        details = request.json
        required_fields = ['username', 'password']
        if not all(field in details for field in required_fields):
            return jsonify({'error': 'Missing required fields'})
        username,password = details['username'],details['password']
        str = database(username=username,password=password,type="signin")
        return jsonify({'response':str})
    elif request.method =='GET':
        return jsonify('signin page')

if __name__ == '__main__':
    app.run(debug=True, port= 5000)