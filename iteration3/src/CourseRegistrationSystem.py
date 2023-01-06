import logging
from SelectionProblem import SelectionProblem


class CourseRegistrationSystem:
    def __init__(self, semester):
        self._semester = semester
        self._logger = logging.getLogger(__name__)

    def registerStudent(self, student):
        padding = 22 * '\u0020'
        self._logger.info(f'\n{padding}○ Registration procees start for the student {student.getID()}')
        transcript = student.getTranscript()
        requestedCourses = student.getRequestedCourses()
        coursesTaken = 0
        for course in requestedCourses:
            if course.getSemester() != self._semester:
                course.getCourseStatistics().incrRegistrationFailureCount()
                description = f"Course is not available at {self._semester}"
                problem = SelectionProblem(0, course, description)
                transcript.addSelectionProblem(problem)
                continue
            prerequisite = course.getPrerequisite()
            if prerequisite:
                prerequisiteInTranscript = transcript.findCourse(prerequisite)
                if prerequisiteInTranscript is None or prerequisiteInTranscript.getTakenCourseStatus() != "Passed":
                    course.getCourseStatistics().incrRegistrationFailureCount()
                    course.getCourseStatistics().incrPrerequisiteProblemCount()
                    description = f"Prerequisite {prerequisite.getName()} isn't passed"
                    self._logger.warning(f' Registration failed: Student with id {student.getID()} can not take {course.getName()} because of failed {prerequisite.getName()}.')
                    self._logger.info(f'\t\t ■  Registration failure count updated for course {course.getName()} --> Problem count:{course.getCourseStatistics().getPrerequisiteProblemCount()}')
                    problem = SelectionProblem(1, course, description)
                    transcript.addSelectionProblem(problem)
                    continue
            if course.getQuota() < 1:
                course.getCourseStatistics().incrQuotaProblemCount()
                course.getCourseStatistics().incrRegistrationFailureCount()
                description = "The quota is exceeded."
                self._logger.warning(f'Registration failed: Student with id {student.getID()} can not take {course.getName()} because of quota problem.')
                self._logger.info(f'\t\t ■  Registration failure count updated for course {course.getName()} --> Problem count:{course.getCourseStatistics().getQuotaProblemCount()}')
                problem = SelectionProblem(2, course, description)
                transcript.addSelectionProblem(problem)
                continue

            if student._advisor.advisorApproval(coursesTaken,student,course) == False: continue 
            
            if student.registerToCourse(course):
                course.getCourseStatistics().incrRegisteredStudentCount()
                course.setQuota(course.getQuota() - 1)
                coursesTaken += 1
                self._logger.info(f'\t Successfully registered. Quota updated for {course.getName()} is {course.getQuota() + 1} to {course.getQuota()}')
        self._logger.info(f' ○ Registration procees end for the student {student.getID()}\n')