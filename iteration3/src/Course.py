import json

class Course:
    def __init__(self):
        self.courseStatistics = CourseStatistics()

    @property
    def ID(self):
        return self.ID

    @ID.setter
    def ID(self, id):
        self.ID = id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def prerequisite(self):
        return self.prerequisite

    @prerequisite.setter
    def prerequisite(self, prerequisite):
        self.prerequisite = prerequisite

    @property
    def prerequisiteId(self):
        return self.prerequisiteId

    @prerequisiteId.setter
    def prerequisiteId(self, prerequisiteId):
        self.prerequisiteId = prerequisiteId

    @property
    def quota(self):
        return self.quota

    @quota.setter
    def quota(self, quota):
        self.quota = quota

    @property
    def credit(self):
        return self.credit

    @credit.setter
    def credit(self, credit):
        self.credit = credit

    @property
    def semester(self):
        return self.semester

    @semester.setter
    def semester(self, semester):
        self.semester = semester

    @property
    def courseStatistics(self):
        return self.courseStatistics