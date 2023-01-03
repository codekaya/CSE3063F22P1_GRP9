from Student import Student
from TakenCourse import TakenCourse
from Course import Course
from SelectionProblem import SelectionProblem
class Transcript:
    
    def __init__(self, student: Student):
        self.student = student
        self.gpa = 0
        self.completedCredit = 0
        self.takenCredit = 0
        self.takenCourses = []
        self.selectionProblems = []

    def addTakenCourse(self, taken_course: TakenCourse):
        status = taken_course.getTakenCourseStatus()
        credit = taken_course.getCourse().getCredit()
        taken_course_in_transcript = self.findCourse(taken_course.getCourse())
        if taken_course_in_transcript is None:
            self.takenCourses.append(taken_course)
            self.takenCredit += credit
            if status == "Passed":
                self.completedCredit += credit
        else:
            if status == "Passed":
                self.completedCredit += credit
            taken_course_in_transcript.setGrade(taken_course.getGrade())
            taken_course_in_transcript.setTakenCourseStatus(taken_course.getTakenCourseStatus())
        self.calculateGpa()
       

    def calculateGpa(self):
        total_credit = 0
        self.gpa = 0
        for taken_course in self.takenCourses:
            if taken_course.getTakenCourseStatus() != "Current":
                credit = taken_course.getCourse().getCredit()
                self.gpa += taken_course.getGrade() * credit
                total_credit += credit
        try:
         self.gpa = self.gpa / total_credit
        except ZeroDivisionError:
         pass

    def findCourse(self, course: Course):
        for taken_course in self.takenCourses:
            if taken_course.getCourse().getName() == course.getName():
                return taken_course
        return None
    
    def getCompletedCredit(self) -> int:
        return self.completedCredit
    
    def getTakenCredit(self) -> int:
        return self.takenCredit
    
    def getSelectionProblems(self):
        return self.selectionProblems
    
    def addSelectionProblem(self, selection_problem: SelectionProblem):
        self.selectionProblems.append(selection_problem)
    
    def getGpa(self) -> float:
        return self.gpa
    
    def getTakenCourses(self):
        return self.takenCourses
