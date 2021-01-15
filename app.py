from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL
from functools import wraps

app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = "later vervangen"

app.config['MYSQL_HOST'] = 'mysql2192.cp.hostnet.nl'
app.config['MYSQL_USER'] = 'u240850_PAdmin'
app.config['MYSQL_PASSWORD'] = '@AdminPolo14'
app.config['MYSQL_DB'] = 'db240850_login'
logged_in = False

def connect():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

def loginrequired(logged_in):
    if logged_in == True:
        return render_template('index.html')
    else:
        return render_template('login.html')

@loginrequired
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
                # If account exists in accounts table in out database
        if account:
            logged_in = True
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg='')

@app.route('/logout')
def logout():
    logged_in = False
    flash('Je bent uitgelogd')


if __name__ == '__main__':
    app.run(debug=True)