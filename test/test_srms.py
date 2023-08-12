        # student_a = Student('John F. Kennedy', 'Politics', 2.8)
        # student_b = Student('Juda Benhur', 'Computer Science', 3.0)
        # student_c = Student('Obed Osei', 'Statistics', 3.5)
        # student_d = Student('Michael Ahor', 'Geography', 3.2)
        # student_e = Student('Desmond Blackmore', 'Statistics', 3.9)
        # student_f = Student('Doh Dormenyo', 'Quantity Survey, 3.6)
        # student_g = Student('Martin Ansah', 'Construction', 3.24)
        # student_h = Student('Enoch Fosu', 'Statistics', 3.4)
        # student_i = Student('Robert Laryea', 'Statistics', 3.4)
#!/usr/bin/python3
'''
test_srms module
'''

import unittest
from models.student import Student
from engine.srms import SRMS


class TestSRMS(unittest.TestCase):
    '''A class to test the Student Record Management System'''

    def setUp(self) -> None:
        self.student_a = Student('John F. Kennedy', 'Politics', 2.8)
        self.student_b = Student('Juda Benhur', 'Computer Science', 3.0)
        self.student_c = Student('Obed Osei', 'Statistics', 3.5)
        self.student_d = Student('Michael Ahor', 'Geography', 3.2)
        self.student_e = Student('Desmond Blackmore', 'Statistics', 3.9)
        self.student_f = Student('Doh Dormenyo', 'Quantity Survey', 3.6)
        self.student_g = Student('Martin Ansah', 'Construction', 3.24)
        self.student_h = Student('Enoch Fosu', 'Statistics', 3.4)
        self.student_i = Student('Robert Laryea', 'Statistics', 3.4)

    def tearDown(self) -> None:
        return super().tearDown()
