import unittest
from InputJSON import InputJSON
from RandomStudent import RandomStudent

class RandomStudentTest(unittest.TestCase):
    def testCreateRandomStudent(self):
        input  = InputJSON()
        random_student = RandomStudent(input)
        student = random_student.createRandomStudent(4, 6)
        isStudentObjectExist = (student is not None)
        self.assertEqual(isStudentObjectExist, True)

if __name__ == '__main__':
    unittest.main()
