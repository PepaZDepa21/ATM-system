import sqlite3
import Customer
from time import sleep

def cursor():
    return sqlite3.connect('database.db').cursor()
c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, amount FLOAT);')
c.connection.close()

def new_customer(customer):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO customer (fname, lname, amount) VALUES (?, ?, 0)', (customer.fname, customer.lname))
    c.execute('SELECT id FROM customer WHERE fname = ? AND lname = ?', (customer.fname, customer.lname))
    i = c.fetchone()
    print(f"Your id is {i[0]}")
    print(f"To access your account you will have to login by your id and your password")
    c.connection.close()
    input("Press enter to continue")


