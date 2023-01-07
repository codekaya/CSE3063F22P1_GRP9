from Student import Student
from Advisor import Advisor
from Transcript import Transcript
import json
import logging
import sys

class OutputJSON:

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def saveStudent(self,student:Student):
        student_dict = {}
        student_dict['ID'] = student.getID()
        student_dict['First Name'] = student.getFirstName()
        student_dict['Last Name'] = student.getLastName()
        student_dict['Semester'] = student.getSemester()
        student_dict['Advisor'] = self.getAdvisorDict(student.getAdvisor())
        student_dict['Transcript'] = self.getTranscriptDict(student.getTranscript())
        student_dict['Requested Courses'] = self.getRequstedCoursedict(student)
        json_object = json.dumps(student_dict, indent = 4,ensure_ascii=False)
        try:
         f = open(f'students/{student.getID()}.json', "w",encoding='utf-8')
        except:
         self._logger.warning('Unexpected error.')
         sys.exit()
        try: 
         f.write(json_object)
        except IOError as e :
         self._logger.warning("I/O error({0}): {1}".format(e.errno, e.strerror))
         sys.exit()
        f.close()
        self._logger.info(f"Student information for {student.getID()} saved successfully in students/{student.getID()}.json")
        
    

    def getAdvisorDict(self,advisor:Advisor):
        advisor_dict = {}
        advisor_dict['ID'] = advisor.getID()
        advisor_dict['First Name'] = advisor.getFirstName()
        advisor_dict['Last Name'] = advisor.getLastName()
        advisor_dict['Email'] = advisor.get_email()
        advisor_dict['Office'] = advisor.get_office()
        return advisor_dict

    def getTranscriptDict(self,tr:Transcript):
        tr_dict = {}
        tr_dict['GPA'] = tr.getGpa()
        tr_dict['Taken Credit'] = tr.getTakenCredit()
        tr_dict['Completed Credit'] = tr.getCompletedCredit()
        taken_courses_arr = []
        for taken_course in tr.getTakenCourses():
            taken_course_dict = {
                'Course ID' : taken_course.getCourse().getID(),
                'Course Name': taken_course.getCourse().getName(),
                'Credit': taken_course.getCourse().getCredit(),
                'Status': taken_course.getTakenCourseStatus(),
                'Grade': taken_course.getGrade()
            }
            taken_courses_arr.append(taken_course_dict)
        tr_dict['Taken Courses'] = taken_courses_arr
        registration_problems_arr = []
        for registration_problem in tr.getSelectionProblems():
            registration_problem_dict = {
                'Problem Id': registration_problem.get_id(),
                'Course' : registration_problem.get_not_registered_course().getName(),
                'Reason' : registration_problem.get_description()
            }
            registration_problems_arr.append(registration_problem_dict)
        tr_dict['Registration Problems'] = registration_problems_arr
        return tr_dict

    def getRequstedCoursedict(self,student:Student):
        rq = []
        for course in student.getRequestedCourses():
         rq_dict = {
            'ID':course.getID(),
            'Course Name': course.getName(),
            'Prerequisite Id': course.getPrerequisiteId(),
            'credit':course.getCredit(),
         }
         rq.append(rq_dict)
        return rq
       

    def saveCourseStatistics(self,courses,semester):
        allCourseStatistics = ''
        for sem in courses:
            for course in sem:
                if course.getSemester() != semester: continue
                allCourseStatistics += str(course.getCourseStatistics())
                print(allCourseStatistics)
        
        try:
         f = open(f'DepartmentStatistics.txt', "w",encoding='utf-8')
        except:
         self._logger.warning('Unexpected error.')
         sys.exit()
        try:
         f.write(allCourseStatistics)
        except IOError as e :
         self._logger.warning("I/O error({0}): {1}".format(e.errno, e.strerror))
         sys.exit()
        f.close()    
       
        
    
        
        