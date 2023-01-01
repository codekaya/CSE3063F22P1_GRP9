import logging
from typing import List

import random

class CourseRegistrationSimulation:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def startSimulation(self):
        input = InputJSON()
        students = self.generateStudents(input)

        registirationSystem = CourseRegistrationSystem(input.getSemester())
        for student in students:
            registirationSystem.registerStudent(student)
        self.logger.info("Students registiration completed")
        output = OutputJSON()
        for student in students:
            output.saveStudent(student)
        output.saveCourseStatistics(input.getCourses(), input.getSemester())
        self.logger.info("Students saved to the json files")

    def generateStudents(self, input: InputJSON):
        randomStudent = RandomStudent(input)
        students = []
        semester = input.getSemester()
        startingSemester = 0
        if semester == "Spring":
            startingSemester += 1
        order = 0
        numberOfStudents = input.getNumberOfStudents()
        for _ in range(numberOfStudents // 4):
            for i in range(startingSemester, 8, 2):
                students.append(randomStudent.createRandomStudent(i, order))
                order += 1
        self.logger.info(f"{numberOfStudents} Random student created")
        return students
