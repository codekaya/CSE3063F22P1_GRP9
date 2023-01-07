import unittest
from Schedule import Schedule

class TestSchedule(unittest.TestCase):
    def testCheckCollision(self):
        s1 = Schedule('Monday','14')
        s2 = Schedule('Sunday','14')

        self.assertEqual(s1.checkCollision(s2),False)
        s2.setDay('Monday')

        self.assertEqual(s2.checkCollision(s1),True)
    
if __name__ == '__main__':
    unittest.main()
