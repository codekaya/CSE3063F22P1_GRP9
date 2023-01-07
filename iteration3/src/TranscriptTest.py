import unittest
from CSE3063F22P1_GRP9 import Advisor, Course, Student, TakenCourse, Transcript

class TranscriptTest(unittest.TestCase):
    def calculateGpaTest(self):
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
        testT.add_taken_course(t1)
        testT.add_taken_course(t2)

        self.assertEqual(expectedGpa, testT.get_gpa())

if __name__ == '__main__':
    unittest.main()
