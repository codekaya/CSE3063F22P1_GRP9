import unittest
from Advisor import Advisor
from Course import Course
from TakenCourse import TakenCourse
from Student import Student
from Transcript import Transcript

class TranscriptTest(unittest.TestCase):
    def testcalculateGpa(self):
        s1 = Course()
        s1.setName("ATA121")
        s1.setCredit(10)
        t1 = TakenCourse(s1, 3, "Passed")

        s2 = Course()
        s2.setName("MBG1201")
        s2.setCredit(5)
        t2 = TakenCourse(s2, 3, "Passed")

        a1 = Advisor("10", "Lionel", "Messi", "deneme@gmail.com", "M2-9")
        st1 = Student("7", "Cristiano", "Ronaldo", 4, a1)

        expectedGpa = 45 / 15

        testT = Transcript(st1)
        testT.addTakenCourse(t1)
        testT.addTakenCourse(t2)

        self.assertEqual(expectedGpa, testT.getGpa(),'Failed.')

if __name__ == '__main__':
    unittest.main()
