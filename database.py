import mysql.connector
from passlib.hash import sha256_crypt


def database(username,password,type,mail=None):
    database = mysql.connector.connect(user = "root",host = "localhost",passwd = "",database = "flask_db")
    cursor = database.cursor()
    if type=='signin':
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, username))
            data = cursor.fetchall()
            cursor.close()
            for user in data:
                if user and sha256_crypt.verify(password, user[3]):
                    return 'Logged in as '+user[1]+' with '+user[2]
            else:
                return 'Invalid credentials'
        except Exception as e:
            print(e)
            return "Error occured"
    elif type=='signup':
        try:
            cursor.execute("SELECT username,email FROM users WHERE username = %s AND email = %s",(username,mail))
            vals = cursor.fetchall()
            if len(vals)!=0:
                cursor.close()
                return "Credentials exists! Try signing In"
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            val = (username,mail,password)
            cursor.execute(sql, val)
            database.commit()
            cursor.close()
            return "Login Credentials saved sucessfully!!"
        except Exception as e:
            print(e)
            return "Exception occured"
        