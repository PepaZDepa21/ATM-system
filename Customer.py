class Customer:
    def __init__(self, id, fname, lname, password, amount):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.amount = amount

class Customer_Insert:
    def __init__(self, fname, lname, password, amount):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.amount = amount
    
class Customer_Login:
    def __init__ (self, id, password):
        self.id = id
        self.password = password