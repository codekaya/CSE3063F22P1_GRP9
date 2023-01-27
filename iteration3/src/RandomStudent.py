import math
from random import randrange
import random
from TakenCourse import TakenCourse
from Transcript import Transcript
from SelectionProblem import SelectionProblem
from Student import Student
import logging

class RandomStudent:
    def __init__(self,input):
        self._input = input
        self._logger = logging.getLogger(__name__)

    def createRandomStudent(self,semester,order):
        Id = self.getRandomId(semester, order)
        Fname = self.getRandomFirstName()
        Lname = self.getRandomLastName()
        advisor = self.getRandomAdvisor()
        student = Student(Id, Fname, Lname, semester + 1, advisor)
        self.createStudentTranscript(semester, student)
        self._logger.info(f'{student.status()} created.')
        return student

    def getRandomId(self, semester, order):
        id = 150118000 + order
        id += 4000 - (int(math.floor((semester + 1) / 2)) * 1000)
        return str(id)

    def getRandomFirstName(self):
        return self._input.getFirstNames()[randrange(0, 399)]

    def getRandomLastName(self):
        return self._input.getLastNames()[randrange(0, 399)]

    def getRandomAdvisor(self):
        return self._input.getAdvisors()[randrange(0,11)]

    def createStudentTranscript(self,semester,student):
        transcript = Transcript(student)
        currentSemester = 'Fall'
        nextSemester = 'Spring'
        selectionProblems = []
        requestedCourses = []
        for i in range(1,semester+2,1):
            requestedCourses.clear()
            takenCourses = transcript.getTakenCourses()
            for j in range(len(takenCourses)):
                takenCourse = takenCourses[j]
                s = takenCourse.getCourse().getSemester()
                if takenCourse.getTakenCourseStatus() == 'Failed' and(s.__eq__(currentSemester) or s.__eq__('Both')):
                    requestedCourses.append(takenCourse.getCourse())
            for j in range(len(selectionProblems)):
                notRegisteredCourse = selectionProblems[j].getNotRegisteredCourse()
                if notRegisteredCourse.getSemester().equals(currentSemester):
                    requestedCourses.append(notRegisteredCourse)
            self.appendCoursesAtSemester(i,requestedCourses)
            if i-1 == semester:
                break
            registeredCourses = self.registerRequestedCourses(requestedCourses,transcript)
            simulatedGrades = self.simulateGrades(registeredCourses)
            for k in range(len(simulatedGrades)):
                transcript.addTakenCourse(simulatedGrades[k])
            tmp = currentSemester
            currentSemester = nextSemester
            nextSemester = tmp
        student.setTranscript(transcript)


    def simulateGrades(self,registeredCourses):
        probabilityOfPassingCourse = self._input.getProbabilityOfPassingCourse()
        takenCourses = []
        for i in range(len(registeredCourses)):
            status = 'Passed'
            grade = 1
            if random.random() > probabilityOfPassingCourse:
                status = 'Failed'
            else:
                grade = random.randint(2,4)    
            takenCourse = TakenCourse(registeredCourses[i],grade,status)
            takenCourses.append(takenCourse)
        return takenCourses

    def registerRequestedCourses(self,requestedCourses,transcript):
        registeredCourses = []
        for course in requestedCourses:
            if course.getPrerequisite() is None:
                registeredCourses.append(course)
                continue
            prerequisiteInTranscript = transcript.findCourse(course.getPrerequisite())
            if prerequisiteInTranscript is None or prerequisiteInTranscript.getTakenCourseStatus() != 'Passed':
                sp = SelectionProblem(None,course,None)
                transcript.addSelectionProblem(sp)
            else:
                registeredCourses.append(course)
        return registeredCourses
    
    def appendCoursesAtSemester(self,semester,requestedCourses):
        semesterCourses = self._input.getCourses()[semester-1]
        for i in range(len(semesterCourses)):
            requestedCourses.append(semesterCourses[i])
