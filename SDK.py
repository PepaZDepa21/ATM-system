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
    
def login():
    cust = int(input("Enter your id: "))
    c = cursor()
    c.execute('SELECT password FROM customer WHERE id = ?', (cust,))
    password = c.fetchone()
    for tries in range(2, -1, -1):
        pas = input("Enter your password: ")
        if tries == 0:
            print("You run out of tries!")
            return 0
        else:    
            if password[0] == pas:
                print("Access to your account has been granted!")
                return cust
            else:
                print(f"Wrong password! You have {tries} left!")
                
def withdraw():
    cust = login()
    if cust == 0 or cust == None:
        pass
    else:
        c = cursor()
        c.execute('SELECT amount FROM customer WHERE id = ?', (cust,))
        amount = c.fetchone()
        print(f"You have {amount[0]} in your account")
        while True:        
            withdraw_amount = float(input("How much would you like to withdraw? "))
            if amount[0] < withdraw_amount:
                print("You don't have enough money to withdraw!")
                continue
            else:
                print(f"You withdrew {amount[0]}$!")
                c = cursor()
                with c.connection:
                    c.execute("UPDATE customer SET amount = ? WHERE id = ?", (amount[0]-withdraw_amount, cust))
                    c.execute("SELECT amount FROM customer WHERE id = ?", (cust,))
                    left = c.fetchone()
                print(f"Now you have {left[0]} in your account!")
                c.connection.close()
            break
        input("Press enter to continue!")
        os.system("CLS")
        
def show_database():
    c = cursor()
    with c.connection:
        c.execute("SELECT * FROM customer")
    e = c.fetchall()
    print(e)
    
def update_money():
    cust = int(input("Enter account id: "))
    amount = float(input("Enter how much you want have in your account: "))
    c = cursor()
    with c.connection:
        c.execute('UPDATE customer SET amount = ? WHERE id = ?', (amount, cust))
    c.execute("SELECT amount FROM customer WHERE id = ?", (cust,))
    a = c.fetchone()
    print(a[0])
    c.connection.close()
    
            
                


