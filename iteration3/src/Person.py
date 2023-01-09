
from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, ID, first_name, last_name):
        self._ID = ID
        self._first_name = first_name
        self._last_name = last_name

    @abstractclassmethod   
    def status(self):
        pass
        
    def getID(self):
        return self._ID
    
    def getFirstName(self):
        return self._first_name
    
    def getLastName(self):
        return self._last_name
