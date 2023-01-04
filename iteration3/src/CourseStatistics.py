class CourseStatistics:
    
    def __init__(self):
        self.registeredStudentCount = 0
        self.registrationFailureCount = 0
        self.quotaProblemCount = 0
        self.prerequisiteProblemCount = 0

    def incrRegisteredStudentCount(self):
        self.registeredStudentCount += 1

    def incrRegistrationFailureCount(self):
        self.registrationFailureCount += 1

    def incrQuotaProblemCount(self):
        self.quotaProblemCount += 1

    def incrPrerequisiteProblemCount(self):
        self.prerequisiteProblemCount += 1

    def getRegisteredStudentCount(self):
        return self.registeredStudentCount

    def getRegistrationFailureCount(self):
        return self.registrationFailureCount

    def getQuotaProblemCount(self):
        return self.quotaProblemCount

    def getPrerequisiteProblemCount(self):
        return self.prerequisiteProblemCount

    def getRateOfSuccessfulRegistration(self):
        return self.registeredStudentCount / (self.registrationFailureCount + self.registeredStudentCount)
