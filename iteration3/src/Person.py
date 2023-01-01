class Person:
    def __init__(self, ID, first_name, last_name):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        
    def status(self):
        raise NotImplementedError("The status method must be implemented by the subclass.")
        
    def get_ID(self):
        return self.ID
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name