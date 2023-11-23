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

def insert(name,lastname,username,password):
    dbConnect()
    add_command = """INSERT INTO USERS(name,lastname,username,password) VALUES {} """
    add = (name,lastname,username,password)
    cursor.execute(add_command.format(add))
    dbOut()
    time.sleep(0.1)

def update_password(newPassword,username):
    dbConnect()
    upd_command = """UPDATE USERS SET password = '{}' WHERE username = '{}'"""
    cursor.execute(upd_command.format(newPassword,username))
    dbOut()
    time.sleep(0.1)

def delete_account(username):
    dbConnect()
    dlt_command = """DELETE FROM USERS WHERE username = '{}' """
    cursor.execute(dlt_command.format(username))
    dbOut()
    time.sleep(0.1)

def drop_database():
    dbConnect()
    drop_command = """DROP DATABASE '{}'"""
    cursor.execute(drop_command.format("database.db"))
    dbOut()



    