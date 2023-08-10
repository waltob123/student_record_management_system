#!/usr/bin/python3
'''
student module
'''

import re
import uuid


class Student:
    '''
    A class that defines a student.
    '''

    def __init__(self, name: str, program: str, gpa: float = 0.0) -> None:
        '''Initializes a new instance of a student

        Args:
            `name (str)`: The name of the student
            `program (str)`: The program of the student
            `gpa (float)`: The current GPA of student

        Return:
            `None`
        '''

        # check data type of arguments
        if not isinstance(name, str):
            raise TypeError(f'{name} must be string')
        if not isinstance(program, str):
            raise TypeError(f'{program} must be string')
        if not isinstance(gpa, float):
            raise TypeError(f'{gpa} must be float')

        # check value of arguments
        if len(name) < 1 or not name.isalpha():
            raise ValueError(f'{name} must not be empty and only characters')
        if len(program) < 1 or not re.fullmatch(r'[a-zA-Z ]+', program):
            raise ValueError(f'{program} must not be empty \
and only characters')

        self.__name = name
        self.__program = program
        self.__gpa = gpa
        self.__id = Student.generate_student_id()
        self.__next = None

    # getters and setters
    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def program(self) -> str:
        return self.__program

    @property
    def gpa(self) -> float:
        return self.__gpa

    @property
    def next(self):
        return self.__next

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f'{name} must be string')
        if len(name) < 1 or not name.isalpha():
            raise ValueError(f'{name} must not be empty and only characters')
        self.__name = name

    @program.setter
    def program(self, program: str) -> None:
        if not isinstance(program, str):
            raise TypeError(f'{program} must be string')
        if len(program) < 1 or not re.fullmatch(r'[a-zA-Z ]+', program):
            raise ValueError(f'{program} must not be empty \
and only characters')
        self.__program = program

    @gpa.setter
    def gpa(self, gpa: float) -> None:
        if not isinstance(gpa, float):
            raise TypeError(f'{gpa} must be float')
        self.__gpa = gpa

    @next.setter
    def next(self, next):
        if isinstance(next, Student) or next is None:
            self.__next = next
        else:
            raise TypeError(f'{next} must be Student')

    @classmethod
    def generate_student_id(cls) -> None:
        '''
        Generates student ID
        '''
        return str(uuid.uuid4())

    def __str__(self) -> str:
        return f'Student <{self.id}> <{self.program}> <{self.gpa}>'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, \
{self.program}, {self.gpa})'
