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

    def __init__(self, name: str, program: str, gpa: float = 0.0,
                 id: str = None) -> None:
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
        if id is not None and not isinstance(id, str):
            raise TypeError(f'{id} must be string')

        # check value of arguments
        if len(name) < 1 or not re.fullmatch(r'[a-zA-Z. ]+', name):
            raise ValueError(f'{name} must not be empty and only characters')
        if len(program) < 1 or not re.fullmatch(r'[a-zA-Z. ]+', program):
            raise ValueError(f'{program} must not be empty \
and only characters')
        if id is not None:
            try:
                new_id = uuid.UUID(id)
            except ValueError as err:
                raise ValueError(f'{id} is not valid')
            self.__id = str(new_id)
        else:
            self.__id = Student.generate_student_id()

        self.__name = name
        self.__program = program
        self.__gpa = gpa
        self.__next = None
        self.__previous = None

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

    @property
    def previous(self):
        return self.__previous

    @name.setter
    def name(self, name_value: str) -> None:
        if not isinstance(name_value, str):
            raise TypeError(f'{name_value} must be string')
        if len(name_value) < 1 or not re.fullmatch(r'[a-zA-Z ]+', name_value):
            raise ValueError(f'{name_value} must not be empty and only characters')
        self.__name = name_value

    @program.setter
    def program(self, program_value: str) -> None:
        if not isinstance(program_value, str):
            raise TypeError(f'{program_value} must be string')
        if len(program_value) < 1 or not re.fullmatch(r'[a-zA-Z ]+', program_value):
            raise ValueError(f'{program_value} must not be empty \
and only characters')
        self.__program = program_value

    @gpa.setter
    def gpa(self, gpa_value: float) -> None:
        if not isinstance(gpa_value, float):
            raise TypeError(f'{gpa_value} must be float')
        self.__gpa = gpa_value

    @next.setter
    def next(self, next_value):
        if isinstance(next_value, Student) or next_value is None:
            self.__next = next_value
        else:
            raise TypeError(f'{next_value} must be Student')

    @previous.setter
    def previous(self, previous_value):
        if isinstance(previous_value, Student) or previous_value is None:
            self.__previous = previous_value
        else:
            raise TypeError(f'{previous_value} must be Student')

    def to_dict(self) -> dict:
        '''converts student attributes to dictionary'''
        student_dict = {}
        student_dict['name'] = self.name
        student_dict['gpa'] = self.gpa
        student_dict['program'] = self.program
        student_dict['next'] = self.next
        student_dict['previous'] = self.previous
        student_dict['id'] = self.id

        return student_dict

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
