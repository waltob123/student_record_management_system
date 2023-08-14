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
        self.srms = SRMS()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_head_assignment(self):
        with self.assertRaises(AttributeError):
            self.srms.head = self.student_a

    def test_insert_student_at_start(self):
        self.assertIsInstance(self.srms.insert_student_at_start
                              (self.student_a), Student)
        with self.assertRaises(Exception):
            self.srms.insert_student_at_start(self.student_a)
        with self.assertRaises(AttributeError):
            self.srms.insert_student_at_start('John')
            self.srms.insert_student_at_start([])
            self.srms.insert_student_at_start(123)
            self.srms.insert_student_at_start(None)
            self.srms.insert_student_at_start('')
            self.srms.insert_student_at_end(Student)

    def test_insert_student_at_position(self):
        with self.assertRaises(Exception):
            self.srms.insert_student_at_position(self.student_c,
                                                 self.student_b.id)
        self.srms.insert_student_at_start(self.student_a)
        with self.assertRaises(Exception):
            self.srms.insert_student_at_position(self.student_c,
                                                 self.student_b.id)
            self.srms.insert_student_at_position(self.student_a,
                                                 self.student_a.id)
        self.assertIsInstance(self.srms.insert_student_at_position
                              (self.student_b, self.student_a.id), Student)
        with self.assertRaises(AttributeError):
            self.srms.insert_student_at_position('', self.student_a)
            self.srms.insert_student_at_position(
                [self.student_d, self.student_e], self.student_a)

    def test_insert_student_at_end(self):
        self.srms.insert_student_at_start(self.student_a)
        self.assertIsInstance(self.srms.insert_student_at_end
                              (self.student_b), Student)
        with self.assertRaises(Exception):
            self.srms.insert_student_at_end(self.student_a)
        with self.assertRaises(AttributeError):
            self.srms.insert_student_at_end([])
            self.srms.insert_student_at_end('')

    def test_search_student(self):
        self.srms.insert_student_at_start(self.student_a)
        self.srms.insert_student_at_start(self.student_b)
        self.srms.insert_student_at_start(self.student_c)
        self.srms.insert_student_at_start(self.student_d)
        self.assertIsNone(self.srms.search_student(self.student_h.id))
        self.assertIsInstance(self.srms.search_student(self.student_a.id),
                              Student)
        self.assertIsNone(self.srms.search_student(None))
        self.assertIsNone(self.srms.search_student(''))

    def test_delete_student(self):
        self.srms.insert_student_at_start(self.student_e)
        self.srms.insert_student_at_start(self.student_f)
        self.srms.insert_student_at_start(self.student_g)
        self.srms.insert_student_at_start(self.student_h)
        self.assertIsInstance(self.srms.delete_student(self.student_e.id),
                              Student)
        self.assertIsNone(self.srms.delete_student(self.student_a.id))
        self.assertIsNone(self.srms.delete_student(None))
        self.assertIsNone(self.srms.delete_student(''))
