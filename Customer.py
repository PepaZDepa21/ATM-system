class Customer:
    def __init__(self, id, fname, lname, password, amount):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.password = password
        self.amount = amount
    
    def __str__(self, id, fname, lname, amount):
        return f"{id} {fname} {lname} {amount}"
    
    def __eq__(self, other):
        return True if self.fname == other.fname and self.lname == other.lname and self.id == other.id else False
    
    __hash__ = None

class Customer_Insert:
    def __init__(self, fname, lname, password, amount):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.amount = amount
    
    def __str__(self, fname, lname, amount):
        return f"{fname} {lname} {amount}"
    
    def __eq__(self, other):
        return True if self.fname == other.fname and self.lname == other.lname and self.id == other.id else False
    
    __hash__ = None