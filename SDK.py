import sqlite3
import Customer
from time import sleep
import os

def cursor():
    return sqlite3.connect('database.db').cursor()
c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, amount FLOAT, password TEXT);')
c.connection.close()

def new_customer(customer):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO customer (fname, lname, amount, password) VALUES (?, ?, 0, ?)', (customer.fname, customer.lname, customer.password))
    c.execute('SELECT id FROM customer WHERE fname = ? AND lname = ?', (customer.fname, customer.lname))
    i = c.fetchone()
    print(f"Your id is {i[0]}")
    print(f"To access your account you will have to login by your id and your password")
    c.connection.close()
    input("Press enter to continue")
    
def login(customer):
    c = cursor()
    c.execute('SELECT password FROM customer WHERE id = ?', (customer.id))
    password = c.fetchone()
    for i in range(3, 0, -1):
        if password == customer.password:
            print("Access to your account has been granted")
            return customer.id
        else:
            if i == 0:
                print("Access denied! You run out of attempts!")
                return 0
            else:
                print(f"Password incorrect! You have {i} attempts left!") 
                
def withdraw(cust_id):
    c = cursor()
    amount = c.execute('SELECT amount FROM customer WHERE id = ?', (cust_id))
    print(f"You have {amount} in your account")
    print("How much would you like to withdraw?")
    withdraw_amount = int(input())
    while True:        
        if amount < withdraw_amount:
            print("You don't have enough money to withdraw!")
            continue
        else:
            print(f"You withdrew {amount}$!")
            c = cursor()
            with c.connection:
                c.execute("UPDATE customer SET amount = ? WHERE id = ?", (amount-withdraw_amount, cust_id))
            left = c.execute("SELECT amount FROM customer WHERE id = ?", (cust_id))
            print(f"Now you have {left} in your account!")
            c.connection.close()
            
                


