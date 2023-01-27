class SelectionProblem:
    def __init__(self, id, not_registered_course, description):
        self._not_registered_course = not_registered_course
        self._id = id
        self._description = description

    def get_id(self):
        return self._id

    def get_not_registered_course(self):
        return self._not_registered_course

    def get_description(self):
        return self._description