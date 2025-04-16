from flask import Flask,request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="smartnotes"
)

cursor = db.cursor(dictionary=True)
@app.route('/signup', methods=['POST'])
def signup():

    data = request.json

    username = data['username']
    email = data['email']
    password = data['password']

    cursor.execute(
        "INSERT INTO users(username,email,password) VALUES(%s,%s,%s)",
        (username,email,password)
    )

    db.commit()

    return jsonify({"success":True})
@app.route('/login', methods=['POST'])
def login():

    data = request.json

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (data['email'],data['password'])
    )

    user = cursor.fetchone()

    if user:
        return jsonify({
            "success":True,
            "username":user["username"]
        })

    return jsonify({"success":False})
@app.route("/")
def home():
    return "Backend Running"

if __name__ == "__main__":
    app.run(debug=True)