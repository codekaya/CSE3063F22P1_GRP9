
from InputJSON import InputJSON
from OutputJSON import OutputJSON
from RandomStudent import RandomStudent
import logging
from CourseRegistrationSystem import CourseRegistrationSystem
import os

class CourseRegistrationSimulation:

    def __init__(self):
        self._logger = logging.getLogger(__name__)
 
    def startSimulation(self):
        input = InputJSON()
        self._logger.info(f'Simulation starterd with the given parameters:\n\t ■ Number of students: {input.getNumberOfStudents()}\n\t ■ Probability of passing course: {input.getProbabilityOfPassingCourse()} \n\t ■ Semester: {input.getSemester()}\n')
        students = self.generateStudents(input)
        
        registrationSystem = CourseRegistrationSystem(input.getSemester())
        for student in students:
            student.selectCourses(input.getCourses())
            registrationSystem.registerStudent(student)
        #Clear students directory
        dir = 'students/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f)) 

        output = OutputJSON()
        for student in students:
                output.saveStudent(student)
        output.saveCourseStatistics(input.getCourses(), input.getSemester())
        self._logger.info('SIMULATION COMPLETED')
    
    def generateStudents(self, input):
        randomStudent = RandomStudent(input)
        students = []
        semester = input.getSemester()
        startingSemester = 0
        if semester == "Spring":
            startingSemester += 1
        order = 0
        numberOfStudents = input.getNumberOfStudents()
        semesters = range(startingSemester, 8, 2)
        sem = 0
        self._logger.info('Random student creation started.')
        for i in range(numberOfStudents):
            students.append(randomStudent.createRandomStudent(semesters[sem], order))
            sem += 1
            order += 1
            if(sem==4):sem=0
        self._logger.info('Random student creation ended.\n')
        return students 
    