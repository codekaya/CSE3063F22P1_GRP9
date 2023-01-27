import unittest
from CourseRegistrationSystem import CourseRegistrationSystem
from RandomStudent import RandomStudent
from InputJSON import InputJSON

class TestCourseRegistrationSystem(unittest.TestCase):
    def setUp(self):
        input = InputJSON()
        self.courses = input.getCourses()
        randomStudent = RandomStudent(input)  
        self.student = randomStudent.createRandomStudent(1,1)
        self.student.selectCourses(input.getCourses())
        
    def testRegisterStudent(self):
        courseRegistrationSystem = CourseRegistrationSystem('Fall')
        courseRegistrationSystem.registerStudent(self.student)
        numberOfSelectionProblems = len(self.student.getTranscript().getSelectionProblems())
        numberOfRegisteredCourses = 0
        for takenCourse in self.student.getTranscript().getTakenCourses():
            if takenCourse.getTakenCourseStatus() == 'Current':
                numberOfRegisteredCourses += 1
        self.assertEqual(numberOfRegisteredCourses+numberOfSelectionProblems == len(self.student.getRequestedCourses()),True)
        for selectionProblem in self.student.getTranscript().getSelectionProblems():
            self.assertEqual(selectionProblem.get_description() != None,True) #Checks if descriptions added 
 
if __name__ == '__main__':
    unittest.main()
