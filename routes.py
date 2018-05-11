#import libraries
from flask import Flask, render_template, request, session, redirect, url_for
import os
import sqlite3
import pandas as pd

#create app
app = Flask(__name__)

DATABASE = 'myapp.db'
def connect_db():
    return sqlite3.connect(DATABASE)

#function for creating escaped double quotes around strings for use in sql
def double_quote(word):
    # return f'"{word}"' # python 3.6 onwards
    return '"{}"'.format(word)

#create url for index or homepage aka route.
@app.route("/")
def index():
    db = connect_db()
    sql = "select person_id, first_name, last_name from people"
    cur = db.execute(sql)
    entries = [dict(person_id=row[0], first_name=row[1],last_name=row[2]) for row in cur.fetchall()]
    print(entries)
    db.close()
    return render_template("profilelist.html",entries=entries)

#create mapping for addprofile form
@app.route("/addprofileform")
def addprofileform():
    return render_template("addprofileform.html")

#create mapping for addprofile
@app.route("/addprofile")
def addprofile():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    db = connect_db()
    sql = "insert into people (first_name,last_name) values (?,?)"
    db.execute(sql,[first_name,last_name])
    db.commit()
    db.close()
    return render_template("index.html",form_first_name=first_name,form_last_name=last_name)

#update profile form

@app.route("/editprofile")
def editprofile():
    person_id = request.args.get('id')
    db = connect_db()
    sql = "select * from people where person_id=%s" % int(float(person_id))
    print(sql)
    result = pd.read_sql_query(sql,db)
    result_dict = result.to_dict()
    db.close()
    return render_template("updateprofileform.html",person=result_dict)

@app.route("/updateprofile")
def updateprofile():
    person_id = int(float(request.args.get('id')))
    first_name = str(request.args.get('first_name'))
    last_name = str(request.args.get('last_name'))

    #first_name = double_quote(first_name)
    #last_name = double_quote(last_name)
    #sql = f"update people set first_name={double_quote(first_name)}, last_name={double_quote(last_name)} where person_id={person_id}"
    #sql = "update people set first_name=%s, last_name=%s where person_id=%s" % (first_name,last_name,person_id)
    #pd.read_sql_query(sql,db)

    db = connect_db()
    sql = "update people set first_name=?, last_name=? where person_id=?"
    db.execute(sql,[first_name,last_name,person_id])
    db.commit()
    db.close()
    return index()

#run the app on localhost port 5000
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
