import json
from Advisor import Advisor
from Course import Course

class InputJSON:
    def __init__(self):
        file = open('parameters.json',encoding='utf-8')
        self.input = json.load(file)
        self.courses = []
        self.readCourses()
    
    def readCourses(self):
        coursesJSON = self.input['courses']
        for i in range(1,9):
            semesterCourses = []
            semester = coursesJSON['s'+str(i)]
            for course in semester:
                c = self.getCourseObject(course)
                semesterCourses.append(c)
            self.courses.append(semesterCourses)
        for semester in self.courses:
            for course in semester:
                if course.getPrerequisiteId() != None:
                    course.setPrerequisite(self.findCourse(course.getPrerequisiteId()))
    
    def getCourseObject(self,courseJSON):
        course = Course()
        course.setID(courseJSON['Course Code'])
        course.setName(courseJSON['Course Name'])
        if courseJSON['Prerequisite']!=None:
            course.setPrerequisiteId(courseJSON['Prerequisite'])
        course.setQuota(courseJSON['Quota'])
        course.setCredit(courseJSON['Credit'])
        course.setSemester(courseJSON['Semester'])
        return course
    
    def findCourse(self,prerequisiteId):
        for semester in self.courses:
            for course in semester:
                if course.getID == prerequisiteId:
                    return course
        return None

    def getAdvisors(self):
        advisors = []
        advisorsJSON = self.input['advisors']
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
        return self.input['firstNames']
    
    def getLastNames(self):
        return self.input['lastNames']
    
    def getCourses(self):
        return self.courses
    
    def getSemester(self):
        return self.input['semester']
        
    def getNumberOfStudents(self):
        return self.input['numberOfStudents']
    
    def getProbabilityOfPassingCourse(self):
        return self.input['probabilityOfPassingCourse']
            