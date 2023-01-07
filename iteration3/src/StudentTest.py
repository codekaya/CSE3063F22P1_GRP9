import unittest
from CSE3063F22P1_GRP9 import Advisor, Student

class StudentTest(unittest.TestCase):
    def ConstructionTest(self):
        sampleAdvisor  = Advisor("109", "Paul", "Walker", "deneme@gmail.com", "M2-9")
        sampleStudent  = Student("150120000", "Jonny", "Deep", 4, sampleAdvisor )

        expectedAdvisorName  = "Paul"
        AdvisorName  = sampleStudent.getAdvisor().getFirstName()

        self.assertEqual(expectedAdvisorName , AdvisorName)

if __name__ == '__main__':
    unittest.main()
