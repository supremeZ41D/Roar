from fastapi import FastAPI
import sqlite3

def kjdb():

    connect = sqlite3.connect('/home/supremez41d/Documents/Python_Folder/LionsRoar/KJ_Bible')
    cursor = connect.cursor()

    return cursor



app = FastAPI()
    
@app.get('/')
def root():
    return {'message': 'Welcome to the King James RestAPI Bible!'}

@app.get('/books/')
def books():

    cursor = kjdb()

    command = """SELECT name
    FROM sqlite_schema
    WHERE type='table' AND name NOT LIKE 'sqlite_%'"""
    
    book_list = cursor.execute(command).fetchall()
    
    return {'books': book_list}

@app.get('/books/{book}')
def book(book):
    cursor = kjdb()

    command = """SELECT *
    FROM Genesis"""

    verse_list = cursor.execute(command).fetchall()

    return {'book': f'{book}',
            'verses': verse_list}
