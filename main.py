from flask import Flask
import mysql.connector as MySQL

app = Flask(__name__)
#mysql = MySQL(app)
app.secret_key = "later vervangen"

app.config['MYSQL_HOST'] = 'mysql2192.cp.hostnet.nl'
app.config['MYSQL_USER'] = 'u240850_PAdmin'
app.config['MYSQL_PASSWORD'] = '@AdminPolo14'
app.config['MYSQL_DB'] = 'db240850_login'

@app.route('/login')
def login():
    return
@app.route('/home')
def home():
    return

if __name__ == '__main__':
    app.run(debug=True)