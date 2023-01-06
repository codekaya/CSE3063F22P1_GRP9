import json
from Advisor import Advisor
from Course import Course
from Schedule import Schedule
import logging
class InputJSON:
    def __init__(self):
        file = open('parameters.json',encoding='utf-8')
        self._input = json.load(file)
        self._courses = []
        self.readCourses()
        self._logger = logging.getLogger(__name__)
    
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
        return self._input['semester']
        
    def getNumberOfStudents(self):
        return self._input['numberOfStudents']
    
    def getProbabilityOfPassingCourse(self):
        return self._input['probabilityOfPassingCourse']     