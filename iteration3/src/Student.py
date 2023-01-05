from Person import Person
from TakenCourse import TakenCourse
from SelectionProblem import SelectionProblem
import json
class Student(Person):
    def __init__(self, Id: str, FName: str, LName: str, semester: int, advisor):
        super().__init__(Id, FName, LName)
        self.semester = semester
        self.advisor = advisor
        self.requested_courses = []
        self.transcript = None
        self._weeklySchedule = []

    def scheduleCourse(self,course):
        for schedule in course.getScheduleList():
            for studentSchedule in self._weeklySchedule:
                if schedule.checkCollision(studentSchedule[0]):
                    description = "Couldn't registered it collides with " + studentSchedule[1].getName()
                    self.transcript.addSelectionProblem(SelectionProblem(4,course,description))
                    return False #There is a collision
        for schedule in course.getScheduleList():
            self._weeklySchedule.append([schedule,course])
        return True #Course is scheduled without collision
                
    def registerToCourse(self,course):
        if self.scheduleCourse(course):
            takenCourse = TakenCourse(course,0,"Current")
            self.transcript.addTakenCourse(takenCourse)
            return True #Student has registered course successfully
        return False #Registration failed because of collision problem
        
    def getSemester(self):
        return self.semester
    
    def getTranscript(self):
        return self.transcript
    
    def getAdvisor(self):
        return self.advisor
    
    def getRequestedCourses(self):
        return self.requested_courses
    
    def addRequestedCourse(self, course):
        self.requested_courses.append(course)
        
    def setTranscript(self, transcript):
        self.transcript = transcript
        
    def status(self):
        print(f"Student in university with id {self.get_ID()} and semester {self.semester}")
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

