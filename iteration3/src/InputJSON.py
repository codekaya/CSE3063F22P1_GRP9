import json
from Advisor import Advisor
from Course import Course
from Schedule import Schedule
import logging
import sys

class InputJSON:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        try:
         file = open('parameters.json',encoding='utf-8')
        except FileNotFoundError:
            self._logger.critical('Parameter file can not found.')
            sys.exit()

        self._input = json.load(file)
        file.close()
        self._courses = []
        self.readCourses()
    
    
    def readCourses(self):
        coursesJSON = self._input['courses']
        for i in range(1,9):
            semesterCourses = []
            semester = coursesJSON['s'+str(i)]
            for course in semester:
                c = self.getCourseObject(course)
                semesterCourses.append(c)
            self._courses.append(semesterCourses)
        for semester in self._courses:
            for course in semester:
                if course.getPrerequisiteId() != None:
                    prereq = self.findCourse(course.getPrerequisiteId())
                    course.setPrerequisite(prereq)
    
    def getCourseObject(self,courseJSON):
        course = Course()
        course.setID(courseJSON['Course Code'])
        course.setName(courseJSON['Course Name'])
        if courseJSON['Prerequisite']!=None:
            course.setPrerequisiteId(courseJSON['Prerequisite'])
        course.setQuota(courseJSON['Quota'])
        course.setCredit(courseJSON['Credit'])
        course.setSemester(courseJSON['Semester'])
        for i in courseJSON['DayTime']:
            day = i['day']
            startingTime = i['time'][0:2]
            course.addSchedule(Schedule(day,startingTime))
        return course
    
    def findCourse(self,prerequisiteId):
        for semester in self._courses:
            for course in semester:
                if course.getID() == prerequisiteId:
                    return course
        return None

    def getAdvisors(self):
        advisors = []
        advisorsJSON = self._input['advisors']
        for i in advisorsJSON:
            fName = i['firstName']
            lName = i['lastName']
            Id = i['id']
            email = i['email']
            office = i['office'] 
            advisor = Advisor(Id,fName,lName,email,office)
            advisors.append(advisor)
        return advisors
        
    def getFirstNames(self):
        return self._input['firstNames']
    
    def getLastNames(self):
        return self._input['lastNames']
    
    def getCourses(self):
        return self._courses
    
    def getSemester(self):
        try:
         semester = self._input['semester']
         if semester != 'Fall' and semester != 'Spring':
            raise Exception('Simulatoin start in Fall or Spring semesters.')
        except Exception as msg:
            self._logger.critical(msg)
            sys.exit()
        return semester

    def setNumberOfStudents(self,number):
        self._input['numberOfStudents'] = number

        
    def getNumberOfStudents(self):
        try:
         student_number = self._input['numberOfStudents']
         if type(student_number) != type(1) or student_number <= 0 :
            raise ValueError('Not a correct type or student number must be greather than 0')
         if student_number > 1000:
            raise Exception(f'{student_number} students too high for simulation. Simulation limitited for up to 1000 students.')
         return self._input['numberOfStudents']

        except ValueError as msg:
            self._logger.critical(msg)
            sys.exit()
        except Exception as msg:
          self._logger.warning(msg)
          self._logger.warning(f'Simulation will continue up until 1000 student.')
          self.setNumberOfStudents(1000)
          return self.getNumberOfStudents()

    def getProbabilityOfPassingCourse(self):
        try:
         prob = float(self._input['probabilityOfPassingCourse'])
         if prob > 1.0 or prob < 0 :
            raise Exception('Probability must be btwn [0,1]')
         return prob
        except ValueError:
         self._logger.critical('Given \'probabilityOfPassingCourse\' is not float type.')
         sys.exit()
        except Exception as msg:
         self._logger.critical(f'{msg}')
         sys.exit()


