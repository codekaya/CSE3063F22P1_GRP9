class Person:
    def __init__(self, ID, first_name, last_name):
        self._ID = ID
        self._first_name = first_name
        self._last_name = last_name
        
    def status(self):
        raise NotImplementedError("The status method must be implemented by the subclass.")
        
    def getID(self):
        return self._ID
    
    def getFirstName(self):
        return self._first_name
    
    def getLastName(self):
        return self._last_name