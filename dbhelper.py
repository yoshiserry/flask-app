#import libraries
from flask import Flask, render_template, request, session, redirect, url_for
import os
import sqlite3
import pandas as pd

DATABASE = 'myapp.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def query_db(query_string):
    db = connect_db()
    result = pd.read_sql_query(query_string,db)
    db.close()
    return result
