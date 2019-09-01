# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class School:
    classes = []

    def __init__(self, classes):
        self.classes = classes

    def get_all_class(self):
        print(*self.classes)


class Class:
    pupils = []
    subjects = {}

    def __init__(self, class_number):
        self.name = class_number

    def add_pupil(self, pupil):
        self.pupils.append(pupil)
        pupil.add_class(self)

    def set_subject(self, teacher):
        self.subjects[teacher.get_subject] = teacher

    def get_pupils(self):
        print(f'Ученики {self.name} класса:')
        for i in self.pupils:
            print(i.get_name())
        return self.pupils

    def get_subjects(self):
        for value in self.subjects.values():
            print(f'предмет: {value.get_subject()}, учитель: {value.get_name()}')

    def __str__(self):
        return self.name


class People:
    def __init__(self, sex, name, surname):
        self.sex = sex
        self.name = name
        self.surname = surname

    def get_name(self):
        return f'{self.name} {self.surname}'


class Pupil(People):
    my_class = None

    def __init__(self, sex, name, surname, parent1, parent2):
        People.__init__(self, sex, name, surname)
        self.parent1 = parent1
        self.parent2 = parent2

    def add_class(self, class_number):
        self.my_class = class_number

    def get_parents(self):
        print(f'{self.parent1.get_name()} и {self.parent2.get_name()}')

    def get_info(self):
        print(f'{self.get_name()} класс {self.my_class}')
        self.my_class.get_subjects()


class Teacher(People):
    def __init__(self, sex, name, surname, subject):
        People.__init__(self, sex, name, surname)
        self.subject = subject

    def get_subject(self):
        return self.subject


class_7A = Class('7A')
class_7B = Class('7B')
class_7C = Class('7C')
school_15 = School([class_7A, class_7B, class_7C])
maria_ivanovna = Teacher('F', 'Мария', 'Герасимовна', 'Математика')
ludmila_petrovna = Teacher('F', 'Людьмила', 'Петровна', 'Русский')
masha = People('F', 'Маша', 'Иванова')
igor = People('M', 'Игорь', 'Иванов')
ivan = Pupil('M', 'Иван', 'Иванов', masha, igor)
class_7A.add_pupil(ivan)
class_7A.set_subject(ludmila_petrovna)
class_7A.set_subject(maria_ivanovna)

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
school_15.get_all_class()
print('*********')
# 2. Получить список всех учеников в указанном классе
class_7A.get_pupils()
print('*********')
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
ivan.get_info()
print('*********')
# 4. Узнать ФИО родителей указанного ученика
ivan.get_parents()
print('*********')
# 5. Получить список всех Учителей, преподающих в указанном классе
class_7A.get_subjects()

