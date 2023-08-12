#!/usr/bin/python3
'''
test_student module
'''

import unittest
from models.student import Student


class TestStudent(unittest.TestCase):
    '''
    A test class that tests the student's model
    '''

    def setUp(self) -> None:
        self.student_a = Student('John F. Kennedy', 'Politics', 2.8)

    def tearDown(self) -> None:
        pass

    def test_instance_initializing(self):
        self.assertIsInstance(self.student_a, Student)
        self.assertRaises(ValueError, Student, name='Juda123 Benhur',
                          program='Computer Science', gpa=3.0)
        self.assertRaises(ValueError, Student, name='Obed Osei',
                          program='Statistics1234', gpa=3.0)
        self.assertRaises(TypeError, Student, name='Michael Ahor',
                          program='Geography', gpa='234')
        self.assertRaises(TypeError, Student, name=[],
                          program='Statistics', gpa=3.9)
        self.assertRaises(TypeError, Student, name='Doh Dormenyo',
                          program=[], gpa=3.6)
        self.assertRaises(ValueError, Student, name='',
                          program='Construction', gpa=3.24)
        self.assertRaises(ValueError, Student, name='Enoch Fosu',
                          program='', gpa=3.4)
        self.assertRaises(ValueError, Student, name='Robert Laryea',
                          program='', gpa=-3.4)
        self.assertRaises(ValueError, Student, name='John Doe',
                          program='Economics', gpa=2.9, id='1234')

    def test_to_dict(self):
        self.assertDictEqual(self.student_a.to_dict(), {
            'name': 'John F. Kennedy',
            'id': self.student_a.id,
            'program': 'Politics',
            'gpa': 2.8,
            'next': None,
            'previous': None,
        })

    def test_next_and_previous(self):
        student_a = Student('John F. Kennedy', 'Politics', 2.8)
        student_b = Student('Juda Benhur', 'Computer Science', 3.0)
        student_c = 1
        student_d = []
        student_a.next = student_b
        student_b.previous = student_a

        self.assertIsInstance(student_a.next, Student)
        with self.assertRaises(TypeError):
            student_b.next = student_c
            student_a.previous = student_d
        self.assertIsNone(student_a.previous)
        self.assertIsInstance(student_b.previous, Student)
