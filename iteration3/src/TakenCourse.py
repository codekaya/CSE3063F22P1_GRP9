class TakenCourse:

    def __init__(self,course,grade,takenCourseStatus):
        self._course = course
        self._grade = grade
        self._takenCourseStatus = takenCourseStatus
    
    def getCourse(self):
        return self._course
    
    def getTakenCourseStatus(self):
        return self._takenCourseStatus
    
    def setTakenCourseStatus(self,takenCourseStatus):
        self._takenCourseStatus = takenCourseStatus
    
    def getGrade(self):
        return self._grade
    
    def setGrade(self,grade):
        self._grade = grade