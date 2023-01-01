import random
from typing import List

class CourseRegistrationSimulation:
    def startSimulation(self):
        input = InputJSON()
        students = self.generateStudents(input)
        
        registrationSystem = CourseRegistrationSystem(input.getSemester())
        for student in students:
            registrationSystem.registerStudent(student)
        
        output = OutputJSON()
        for student in students:
            output.saveStudent(student)
        output.saveCourseStatistics(input.getCourses(), input.getSemester())
    
    def generateStudents(self, input: InputJSON) -> List[Student]:
        randomStudent = RandomStudent(input)
        students = []
        semester = input.getSemester()
        startingSemester = 0
        if semester == "Spring":
            startingSemester += 1
        order = 0
        numberOfStudents = input.getNumberOfStudents()
        for j in range(numberOfStudents // 4):
            for i in range(startingSemester, 8, 2):
                students.append(randomStudent.createRandomStudent(i, order))
                order += 1
        return students
