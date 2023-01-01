class SelectionProblem:
    def __init__(self, not_registered_course, Id=None, description=None):
        self.Id = Id
        self.not_registered_course = not_registered_course
        self.description = description
        
    def get_id(self):
        return self.Id
    
    def get_not_registered_course(self):
        return self.not_registered_course
    
    def get_description(self):
        return self.description