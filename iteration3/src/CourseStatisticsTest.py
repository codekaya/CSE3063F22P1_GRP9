import unittest
from CSE3063F22P1_GRP9 import CourseStatistics


class CourseStatisticsTest(unittest.TestCase):
    def getRateOfSucessfullRegistraion(self):
        csTesting = CourseStatistics()

        for i in range(5):
            csTesting.incrRegisteredStudentCount()

        for i in range(1):
            csTesting.incrRegistrationFailureCount()

        registeredStudentCount = csTesting.getRegisteredStudentCount()
        registrationFailureCount = csTesting.getRegistrationFailureCount()

        rateOfSucessfullRegistraion = (1.0 * registeredStudentCount) / (
                    registrationFailureCount + registeredStudentCount)

        self.assertEqual(rateOfSucessfullRegistraion, csTesting.getRateOfSuccessfulRegistration())


if __name__ == '__main__':
    unittest.main()
