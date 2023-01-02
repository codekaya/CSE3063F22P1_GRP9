class CourseRegistrationSystem:
    def __init__(self, semester):
        self.semester = semester
        self.MAX_COURSE_COUNT = 10

    def registerStudent(self, student):
        transcript = student.getTranscript()
        requestedCourses = student.getRequestedCourses()
        coursesTaken = 0
        for course in requestedCourses:
            if course.getSemester() != self.semester:
                course.getCourseStatistics().incrRegistrationFailureCount()
                description = f"Course is not available at {self.semester}"
                problem = SelectionProblem(0, course, description)
                transcript.addSelectionProblem(problem)
                continue
            prerequisite = course.getPrerequisite()
            if prerequisite is not None:
                prerequisiteInTranscript = transcript.findCourse(prerequisite)
                if prerequisiteInTranscript is None or prerequisiteInTranscript.getTakenCourseStatus() != "Passed":
                    course.getCourseStatistics().incrPrerequisiteProblemCount()
                    course.getCourseStatistics().incrPrerequisiteProblemCount()
                    description = f"Prerequisite {prerequisite.getName()} isn't passed"
                    problem = SelectionProblem(1, course, description)
                    transcript.addSelectionProblem(problem)
                    continue
            if course.getQuota() < 1:
                course.getCourseStatistics().incrQuotaProblemCount()
                course.getCourseStatistics().incrRegistrationFailureCount()
                description = "The quota is exceeded."
                problem = SelectionProblem(2, course, description)
                transcript.addSelectionProblem(problem)
                continue
            if coursesTaken > self.MAX_COURSE_COUNT:
                course.getCourseStatistics().incrRegistrationFailureCount()
                description = "Student can't take more than 10 courses at one semester."
                problem = SelectionProblem(3, course, description)
                transcript.addSelectionProblem(problem)
                continue
            course.getCourseStatistics().incrRegisteredStudentCount()
            TakenCourse = TakenCourse(course, 0, "Current")
            transcript.addTakenCourse(TakenCourse)
            course.setQuota(course.getQuota() - 1)
            coursesTaken += 1
