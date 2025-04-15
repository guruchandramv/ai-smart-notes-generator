from flask import Flask
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

@app.route("/")
def home():
    return "Backend Running"

if __name__ == "__main__":
    app.run(debug=True)