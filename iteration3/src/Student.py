from Person import Person
import json
class Student(Person):
    def __init__(self, Id: str, FName: str, LName: str, semester: int, advisor):
        super().__init__(Id, FName, LName)
        self.semester = semester
        self.advisor = advisor
        self.requested_courses = []
        self.transcript = None
        
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