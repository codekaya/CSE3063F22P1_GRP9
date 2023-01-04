class TakenCourse:

    def __init__(self,course,grade,takenCourseStatus):
        self.course = course
        self.grade = grade
        self.takenCourseStatus = takenCourseStatus
    
    def getCourse(self):
        return self.course
    
    def getTakenCourseStatus(self):
        return self.takenCourseStatus
    
    def setTakenCourseStatus(self,takenCourseStatus):
        self.takenCourseStatus = takenCourseStatus
    
    def getGrade(self):
        return self.grade
    
    def setGrade(self,grade):
        self.grade = grade