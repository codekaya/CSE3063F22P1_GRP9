from typing import List

class Student(Person):
    def __init__(self, Id: str, FName: str, LName: str, semester: int, advisor):
        super().__init__(Id, FName, LName)
        self.semester = semester
        self.advisor = advisor
        self.requested_courses = []
        self.transcript = None
        
    def get_semester(self):
        return self.semester
    
    def get_transcript(self):
        return self.transcript
    
    def get_advisor(self):
        return self.advisor
    
    def get_requested_courses(self) -> List[Course]:
        return self.requested_courses
    
    def add_requested_course(self, course):
        self.requested_courses.append(course)
        
    def set_transcript(self, transcript):
        self.transcript = transcript
        
    def status(self):
        print(f"Student in university with id {self.get_ID()} and semester {self.semester}")