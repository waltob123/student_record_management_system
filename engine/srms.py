#!/usr/bin/python3
'''
student_record_management_system module
'''

from models.student import Student


class SRMS:
    '''A class that defines the Student
    Record Management System.
    '''

    def __init__(self) -> None:
        '''Initializes a Student Record Management System
        with head equal to None'''
        self.head = None

    def insert_student_at_start(self, student: Student) -> str:
        '''
        Inserts a student at the start of linked list.

        Args:
            `student (Student)`: student object to insert

        Return:
            `message (str)`: success or failure
        '''
        # check if head is empty
        if self.search_student(student.id):
            return f'Student {student.id} already exists!'

        if self.head is None and not self.search_student(student.id):
            self.head = student
            return f'Student {student.id} added successfully!'

        if not self.search_student(student.id):
            temp = self.head
            self.head = student
            temp.previous = student
            student.next = temp
            return f'Student {student.id} added successfully!'

    def insert_student_at_position(self, student: Student,
                                   student_id: str) -> str:
        '''
        Inserts a student at a position

        Args:
            `student (Student)`: student object to insert
            `student_id` (str): where to insert student object

        Return:
            `message (str)`: success or failure
        '''
        if self.search_student(student.id):
            return f'Student {student.id} already exists!'

        if self.head is None:
            self.insert_student_at_start(student)
            return f'Student {student.id} added successfully!'
        else:
            student_position = self.search_student(student_id)
            temp = student_position # set student_position to temp
            temp.previous.next = student # set the next value of the temp' next to student
            student.previous = temp.previous # set the student's previous to temp's previous
            student.next = temp # set student's next value to temp
            temp.previous = student # set temp's previous to student
            return f'Student {student.id} added successfully!'

    def insert_student_at_end(self, student: Student) -> str:
        '''
        Inserts a student at the end of linked list

        Args:
            `student (Student)`: student object to insert

        Return:
            `message (str)`: success or failure
        '''
        if self.search_student(student.id):
            return f'Student {student.id} already exists!'

        if self.head is not None:
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = student
            student.previous = temp
            return f'Student {student.id} added successfully!'
        else:
            self.insert_student_at_start(student)

    def search_student(self, student_id: str) -> Student:
        '''
        Searches for a student in linked list

        Args:
            `student_id (str)`: student to search for

        Return:
            `Student or False`: student object or False
        '''
        if self.head is not None:
            temp = self.head

            while temp is not None:
                if temp.id == student_id:
                    return temp
                else:
                    temp = temp.next
        return None

    def view_all_students(self) -> None:
        '''
        prints all students to screen
        '''
        if self.head is None:
            print('No students available!')
        else:
            temp = self.head

            while temp is not None:
                print(temp)
                temp = temp.next

    def delete_student(self, student_id: str) -> None:
        '''
        Deletes a student from the linked list.

        Args:
            `student_id (str)`: student to delete
        '''
        student = self.search_student(student_id)
        if not student:
            return None
        if student.id == self.head.id:
            self.head = self.head.next
            self.head.previous = None
        else:
            student.previous.next = student.next
        return student
