import sqlite3 as sql
import time

def dbConnect():
    global connect
    connect = sql.connect("database.db")
    global cursor
    cursor = connect.cursor()

def dbOut():
    connect.commit()
    connect.close()
    time.sleep(0.5)


def create():
    dbConnect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY NOT NULL,
        name varchar(75) NOT NULL,
        lastname varchar(75) NOT NULL,
        username text NOT NULL,
        password text NOT NULL
    )""")
    dbOut()
    time.sleep(0.2)


# def insert(name, lastname, username, password):
#     dbConnect()
#     comment = "INSERT INTO USERS (name, lastname, username, password) VALUES (?, ?, ?, ?)"
#     cursor.execute(comment, (name, lastname, username, password))
#     dbOut()

def insert(name,lastname,username,password):
    dbConnect()
    add_command = """INSERT INTO USERS(name,lastname,username,password) VALUES {} """
    add = (name,lastname,username,password)
    cursor.execute(add_command.format(add))
    dbOut()
    time.sleep(0.1)
insert("cem","yurtsever0","cy","1546")