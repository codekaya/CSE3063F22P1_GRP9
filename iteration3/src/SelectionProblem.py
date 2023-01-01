class SelectionProblem:
    def __init__(self, not_registered_course):
        self.not_registered_course = not_registered_course
        self.id = None
        self.description = None

    def __init__(self, id, not_registered_course, description):
        self.not_registered_course = not_registered_course
        self.id = id
        self.description = description

    def get_id(self):
        return self.id

    def get_not_registered_course(self):
        return self.not_registered_course

    def get_description(self):
        return self.description