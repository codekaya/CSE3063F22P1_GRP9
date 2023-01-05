
from CourseStatistics import CourseStatistics

class Course:

    def __init__(self):
        self.courseStatistics = CourseStatistics()
        self.ID = 0 
        self.name = ''
        self.prerequisite = None
        self.prerequisiteId = None
        self.quota = 0
        self.credit = 0
        self.semsester = ''


    def getID(self):
        return self.ID

    
    def setID(self, id):
        self.ID = id

    
    def getName(self):
        return self.name

    
    def setName(self, name):
        self.name = name

   
    def getPrerequisite(self):
        return self.prerequisite

   
    def setPrerequisite(self, prerequisite):
        self.prerequisite = prerequisite

    
    def getPrerequisiteId(self):
        return self.prerequisiteId

    
    def setPrerequisiteId(self, prerequisiteId):
        self.prerequisiteId = prerequisiteId

    def getQuota(self):
        return self.quota

   
    def setQuota(self, quota):
        self.quota = quota

   
    def getCredit(self):
        return self.credit

   
    def setCredit(self, credit):
        self.credit = credit

   
    def getSemester(self):
        return self.semester

   
    def setSemester(self, semester):
        self.semester = semester

    
    def getCourseStatistics(self):
        return self.courseStatistics