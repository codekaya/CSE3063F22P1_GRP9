
from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, ID, first_name, last_name):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name

    @abstractclassmethod   
    def status(self):
        pass
        
    def getID(self):
        return self.ID
    
    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name