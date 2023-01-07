import unittest
from CSE3063F22P1_GRP9 import InputJSON, RandomStudent, Student

class RandomStudentTest(unittest.TestCase):
    def CreateRandomStudentTest(self):
        input  = InputJSON()
        random_student = RandomStudent(input)
        student = random_student.createRandomStudent(4, 6)
        isStudentObjectExist = (student is not None)
        self.assertEqual(isStudentObjectExist, True)

if __name__ == '__main__':
    unittest.main()
