from Person import Person
from SelectionProblem import SelectionProblem
import logging

class Advisor(Person):
    def __init__(self, ID, firstName, lastName, email, office):
        super().__init__(ID, firstName, lastName)
        self._email = email
        self._office = office
        self._logger = logging.getLogger(__name__)

    def advisorApproval(self,coursesTaken,student,course):
        if coursesTaken > 10:
            course.getCourseStatistics().incrRegistrationFailureCount()
            course.getCourseStatistics().incrMaxcourseProblemCount()
            description = "Student can't take more than 10 courses at one semester."
            self._logger.warning(f' Registration failed [ADVISOR]: {self.status()} did not approve registration. {student.status()} can not take {course.getName()} because of course limit exceed.')
            self._logger.info(f'\t\t ■  Registration failure count updated for course {course.getName()} --> Problem count:{course.getCourseStatistics().getRegistrationFailureCount()}')
            problem = SelectionProblem(3, course, description)
            student._transcript.addSelectionProblem(problem)
            return False
        return True
    
    def get_email(self):
        return self._email

    def get_office(self):
        return self._office

    def status(self):
       return f'Advisor {self.getFirstName()} {self.getLastName()}'

    

 
