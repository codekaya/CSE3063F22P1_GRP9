
from CourseStatistics import CourseStatistics

class Course:

    def __init__(self):
        self._courseStatistics = CourseStatistics(self)
        self._ID = 0 
        self._name = ''
        self._prerequisite = None
        self._prerequisiteId = None
        self._quota = 0
        self._credit = 0
        self._semsester = ''
        self._scheduleList = []
    
    def checkCollision(self,course):
        for schedule in self._scheduleList:
            for schedule2 in course.getScheduleList():
                if(schedule.checkCollision(schedule2)):
                    return True #Courses collides
        return False #No collision
    
    def getID(self):
        return self._ID

    
    def setID(self, id):
        self._ID = id

    
    def getName(self):
        return self._name

    
    def setName(self, name):
        self._name = name

   
    def getPrerequisite(self):
        return self._prerequisite

   
    def setPrerequisite(self, prerequisite):
        self._prerequisite = prerequisite

    
    def getPrerequisiteId(self):
        return self._prerequisiteId

    
    def setPrerequisiteId(self, prerequisiteId):
        self._prerequisiteId = prerequisiteId

    def getQuota(self):
        return self._quota

   
    def setQuota(self, quota):
        self._quota = quota

   
    def getCredit(self):
        return self._credit

   
    def setCredit(self, credit):
        self._credit = credit

   
    def getSemester(self):
        return self._semester

   
    def setSemester(self, semester):
        self._semester = semester

    
    def getCourseStatistics(self):
        return self._courseStatistics

    def getScheduleList(self):
        return self._scheduleList
    
    def addSchedule(self,schedule):
        self._scheduleList.append(schedule)