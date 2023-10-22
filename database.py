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

create()