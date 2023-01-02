import Person

class Advisor(Person):
    def __init__(self, ID, firstName, lastName, email, office):
        super().__init__(ID, firstName, lastName)
        self.email = email
        self.office = office

    def getEmail(self):
        return self.email

    def getOffice(self):
        return self.office

    def status(self):
        print(f"Advisor in university with id {self.ID} and email {self.office}")
