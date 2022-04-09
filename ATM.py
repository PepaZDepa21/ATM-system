import SDK
from Customer import Customer, Customer_Insert

option = """
Choose your option
1. new customer
2. withdraw money
3. insert money
4. quit
"""

while True:
    print(option)
    op = int(input())
    if op == 1:
        fname = input("Your first name: ")
        lname = input("Your last name: ")
        password = input("Enter your password: ")
        customer = Customer_Insert(fname, lname, password, 0)
        SDK.new_customer(customer)
    
    elif op == 2:
        pass
    
    elif op == 3:
        pass
    
    elif op == 4:
        break  
