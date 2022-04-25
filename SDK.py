import sqlite3
import Customer
import os

def cursor():
    return sqlite3.connect('database.db').cursor()
c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, amount FLOAT, password TEXT);')
c.execute('CREATE TABLE IF NOT EXISTS admin (password TEXT);')
c.execute('INSERT INTO admin (password) VALUES ("CaukyMnauky123")')
c.connection.commit()
c.connection.close()

def new_customer(customer):
    os.system("CLS")
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO customer (fname, lname, amount, password) VALUES (?, ?, 0, ?)', (customer.fname, customer.lname, customer.password))
    c.execute('SELECT id FROM customer WHERE fname = ? AND lname = ?', (customer.fname, customer.lname))
    i = c.fetchone()
    print(f"Your id is {i[0]}")
    print(f"To access your account you will have to login by your id and your password")
    c.connection.close()
    input("Press enter to continue")
    os.system("CLS")
    
def login():
    try:
        cust = int(input("Enter your id: "))
    except:
        print("Wrong symbol! You have to enter number!")
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
    os.system("CLS")
    cust = login()
    if cust == 0 or cust == None:
        pass
    else:
        c = cursor()
        c.execute('SELECT amount FROM customer WHERE id = ?', (cust,))
        amount = c.fetchone()
        print(f"You have {amount[0]}$ in your account")
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
                    balance = c.fetchone()
                print(f"Now you have {balance[0]}$ in your account!")
                c.connection.close()
            break
        input("Press enter to continue!")
        os.system("CLS")
        
def insert():
    os.system("CLS")
    cust = login()
    if cust == 0 or cust == None:
        pass
    else:
        c = cursor()
        c.execute('SELECT amount FROM customer WHERE id = ?', (cust,))
        amount = c.fetchone()
        print(f"You have {amount[0]}$ in your account")       
        insert_amount = float(input("How much would you like to insert? "))
        print(f"You inserted {insert_amount}$!")
        c = cursor()
        with c.connection:
            c.execute("UPDATE customer SET amount = ? WHERE id = ?", (amount[0]+insert_amount, cust))
        c.execute("SELECT amount FROM customer WHERE id = ?", (cust,))
        balance = c.fetchone()
        print(f"Now you have {balance[0]}$ in your account!")
        c.connection.close()
    input("Press enter to continue!")
    os.system("CLS")

def turn_off():
    c = cursor()
    with c.connection:
        c.execute("SELECT password FROM admin")
        pas = c.fetchone()
    c.connection.close()
    for tries in range(2, -1, -1):
        e_pas = input("Enter your password: ")
        if tries == 0:
            os.system("CLS")
            return True
        else:    
            if e_pas == pas[0]:
                os.system("CLS")
                return False
            else:
                print(f"Wrong password! You have {tries} left!")