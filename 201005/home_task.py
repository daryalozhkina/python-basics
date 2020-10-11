class Student: # upper CamelCase
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.birthdate = None
        self.group = None

class Teacher:
    def __init__(self):
        self.surname = None
        self.name = None
        self.patronymic = None
        self.discipline = None


class Group:
    def __init__(self):
        self.specialty = None
        self.number_of_students = None
        self.patronymic = None
        self.curator = None


class College:
    def __init__(self):
        self.administration = None
        self.teacher = None
        self.training_group = None
        self.number_of_students = None
        self.discipline = None


class Examination:
    def __init__(self):
        self.teacher = None
        self.discipline = None
        self.mark = None


class Student_on_the_exam:
    def __init__(self):
        self.gradebook = None
        self.discipline = None
        self.mark = None


class Car:
    def __init__(self):
        self.type = None
        self.color = None