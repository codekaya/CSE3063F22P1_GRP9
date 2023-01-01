import Student
import TakenCourse
import Course
import SelectionProblem
class Transcript:
    
    def __init__(self, student: Student):
        self.student = student
        self.gpa = 0
        self.completedCredit = 0
        self.takenCredit = 0
        self.takenCourses = []
        self.selectionProblems = []

    def add_taken_course(self, taken_course: TakenCourse):
        status = taken_course.get_taken_course_status()
        credit = taken_course.get_course().get_credit()
        taken_course_in_transcript = self.find_course(taken_course.get_course())
        if taken_course_in_transcript is None:
            self.takenCourses.append(taken_course)
            self.takenCredit += credit
            if status == "Passed":
                self.completedCredit += credit
        else:
            if status == "Passed":
                self.completedCredit += credit
            taken_course_in_transcript.set_grade(taken_course.get_grade())
            taken_course_in_transcript.set_taken_course_status(taken_course.get_taken_course_status())
        self.calculate_gpa()
       

    def calculate_gpa(self):
        total_credit = 0
        self.gpa = 0
        for taken_course in self.takenCourses:
            if taken_course.get_taken_course_status() != "Current":
                credit = taken_course.get_course().get_credit()
                self.gpa += taken_course.get_grade() * credit
                total_credit += credit
        self.gpa = self.gpa / total_credit
        

    def find_course(self, course: Course):
        for taken_course in self.takenCourses:
            if taken_course.get_course().get_name() == course.get_name():
                return taken_course
        return None
    
    def get_completedCredit(self) -> int:
        return self.completedCredit
    
    def get_takenCredit(self) -> int:
        return self.takenCredit
    
    def get_selectionProblems(self):
        return self.selectionProblems
    
    def add_selection_problem(self, selection_problem: SelectionProblem):
        self.selectionProblems.append(selection_problem)
    
    def get_gpa(self) -> float:
        return self.gpa
    
    def get_takenCourses(self):
        return self.takenCourses
