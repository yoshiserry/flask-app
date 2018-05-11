import sqlite3
from flask import Flask

#create app
app = Flask(__name__)

DATABASE = 'myapp.db'

def init_db():
    db = sqlite3.connect(DATABASE)
    with app.open_resource('db.sql',mode='r') as f:
        sql = f.read()

    print(sql)
    db.cursor().execute(sql)
    db.commit()
    db.close()

#run the app on localhost port 5000
if __name__ == '__main__':
    init_db()
