class CourseStatistics:
    
    def __init__(self,course):
        self._course = course
        self._registeredStudentCount = 0
        self._registrationFailureCount = 0
        self._quotaProblemCount = 0
        self._prerequisiteProblemCount = 0
        self._collisionProblemCount = 0
        self._maxcourseProblemCount = 0

    def __str__(self):
        s = f' -->  {self._course.getID().upper()} {self._course.getName().upper()}\n\n'
        s += "\t■ Number of students applied for course :"+str(self.getRegisteredStudentCount() + self.getRegistrationFailureCount())+"\n"
        s += "\t■ Number of registered students:"+str(self.getRegisteredStudentCount())+"\n"
        s += "\t■ Number of registration failures:"+str(self.getRegistrationFailureCount())+"\n"
        s += "\t - Number of quota problems:"+str(self.getQuotaProblemCount())+"\n"
        s += "\t - Number of prerequisite problems:"+str(self.getPrerequisiteProblemCount())+"\n"
        s += "\t - Number of collision problems:"+str(self.getCollisionProblemCount())+"\n"
        s += "\t - Number of max limit course problems:"+str(self.getMaxcourseProblemCount())+"\n\n"
        return s
        
    def incrRegisteredStudentCount(self):
        self._registeredStudentCount += 1

    def incrRegistrationFailureCount(self):
        self._registrationFailureCount += 1

    def incrQuotaProblemCount(self):
        self._quotaProblemCount += 1

    def incrPrerequisiteProblemCount(self):
        self._prerequisiteProblemCount += 1
    
    def incrCollisionProblemCount(self):
        self._collisionProblemCount += 1
    
    def incrMaxcourseProblemCount(self):
        self._maxcourseProblemCount +=1

    def getRegisteredStudentCount(self):
        return self._registeredStudentCount

    def getRegistrationFailureCount(self):
        return self._registrationFailureCount

    def getQuotaProblemCount(self):
        return self._quotaProblemCount

    def getPrerequisiteProblemCount(self):
        return self._prerequisiteProblemCount
    
    def getCollisionProblemCount(self):
        return self._collisionProblemCount

    def getMaxcourseProblemCount(self):
        return self._maxcourseProblemCount

