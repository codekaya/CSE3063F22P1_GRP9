from Person import Person
from TakenCourse import TakenCourse
from SelectionProblem import SelectionProblem
import logging
class Student(Person):
    def __init__(self, Id: str, FName: str, LName: str, semester: int, advisor):
        super().__init__(Id, FName, LName)
        self._semester = semester
        self._advisor = advisor
        self._requested_courses = []
        self._transcript = None
        self._weeklySchedule = []
        self._logger = logging.getLogger(__name__)

    def scheduleCourse(self,course):
        for schedule in course.getScheduleList():
            for studentSchedule in self._weeklySchedule:
                if schedule.checkCollision(studentSchedule[0]):
                    description = "Couldn't registered it collides with " + studentSchedule[1].getName()
                    course.getCourseStatistics().incrRegistrationFailureCount()
                    course.getCourseStatistics().incrCollisionProblemCount()
                    self._logger.warning(f' Registration failed: Student with id {self.getID()} can not take {course.getName()} because it collides with {studentSchedule[1].getName()}')
                    self._logger.info(f'\t\t ■  Registration failure count updated for course {course.getName()} --> Problem count:{course.getCourseStatistics().getCollisionProblemCount()}')
                    self._transcript.addSelectionProblem(SelectionProblem(4,course,description))
                    return False #There is a collision
        for schedule in course.getScheduleList():
            self._weeklySchedule.append([schedule,course])
        return True #Course is scheduled without collision
                
    def registerToCourse(self,course):
        if self.scheduleCourse(course):
            takenCourse = TakenCourse(course,0,"Current")
            self._transcript.addTakenCourse(takenCourse)
            return True #Student has registered course successfully
        return False #Registration failed because of collision problem

    def selectCourses(self,courses):
        for takenCourse in self._transcript.getTakenCourses():
            if takenCourse.getTakenCourseStatus() == 'Failed':
                self._requested_courses.append(takenCourse.getCourse())
        for selectionProblem in self._transcript.getSelectionProblems():
            notRegisteredCourse = selectionProblem.get_not_registered_course()
            self._requested_courses.append(notRegisteredCourse)
        self._transcript.getSelectionProblems().clear()
        for course in courses[self._semester-1]:
            self._requested_courses.append(course)
        self._logger.info(f'◉ Random sutdent with id:{self.getID()},semester:{self._semester + 1} and requested courses list:' )
        for course in self.getRequestedCourses():
            self._logger.info(f'\t{course.getName()} → Quota:{course.getQuota()}' )
            if course.getPrerequisite() is not None:
             self._logger.info(f'\t   ■  Prerequiste(s):{course.getPrerequisite().getName()}')
        
    def getSemester(self):
        return self._semester
    
    def getTranscript(self):
        return self._transcript
    
    def getAdvisor(self):
        return self._advisor
    
    def getRequestedCourses(self):
        return self._requested_courses
    
    def addRequestedCourse(self, course):
        self._requested_courses.append(course)
        
    def setTranscript(self, transcript):
        self._transcript = transcript
        
    def status(self):
        print(f"Student in university with id {self.getID()} and semester {self._semester}")
    

