from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)
app.secret_key = 'your_secret_key'

mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sherin611'
app.config['MYSQL_DB'] = 'Employees'
mysql.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def view():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM employee')
    cursor.fetchall()
    return render_template('home.html')
    
@app.route('/add', methods=['POST'])
def add():
    name=request.form['name']
    email=request.form['email']
    department=request.get_data['Engineering','HR','Sales']
    salary=request.form['salary']
    date=request.form['date']
    
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO employee(name,email,department,salary,joining_date) values (%s,%s,%s,%s,%s)',(name,email,department,salary,date))
    mysql.connection.commit()
    return render_template('home.html')

@app.route('/update<id>' , method=['POST'])
def update(id):
    name=request.form['name']
    email=request.form['email']
    department=request.form['department']
    salary=request.form['salary']
    date=request.form['date']
    
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('UPDATE employee SET name=%s where id=%s ',(id,name))
    cursor.execute('UPDATE employee SET email=%s where id=%s ',(id,email))
    cursor.execute('UPDATE employee SET department=%s where id=%s ',(id,department))
    cursor.execute('UPDATE employee SET salary=%s where id=%s ',(id,salary))
    cursor.execute('UPDATE employee SET date=%s where id=%s ',(id,date))
    
    mysql.connection.commit()
    return render_template('home.html')

@app.route('/delete<id>', method=['DELETE'])
def delete(id):
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(' DELETE FROM employee where id=%d',(id))
    mysql.connection.commit()
    return render_template('home.html')

   
app.run(debug=True)