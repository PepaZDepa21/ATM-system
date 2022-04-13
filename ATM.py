import os
import SDK
from Customer import Customer_Insert, Customer_Login

option = """
Choose your option
1. new customer
2. withdraw money
3. insert money
4. quit
"""

os.system("CLS")

while True:
    print(option)
    op = int(input())
    if op == 1:
        os.system("CLS")
        fname = input("Your first name: ")
        lname = input("Your last name: ")
        password = input("Enter your password: ")
        customer = Customer_Insert(fname, lname, password, 0)
        SDK.new_customer(customer)
    
    elif op == 2:
        os.system("CLS")
        SDK.withdraw()
      
            
    elif op == 3:
        os.system("CLS")
        num = int(input("Enter your id: "))
        password = input("Enter your password: ")
        customer = Customer_Login(num, password)
        SDK.login(customer)
        
    elif op == 4:
        break 
    
    os.system("CLS") 
