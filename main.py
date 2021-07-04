class Student:
    average_rating = 0

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_for_lecturer(self, lecturer, course, lecturer_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.teach_grades:
                lecturer.teach_grades[course] += [lecturer_grade]
            else:
                lecturer.teach_grades[course] = [lecturer_grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        self.average_rating += round((sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))), 2)
        return self.average_rating

    def __str__(self):
        for_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return for_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_rating > other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teach_grades = {}
        self.average_l_rating = 0

    def average_lectors_rate(self):
        self.average_l_rating += round((sum(sum(self.teach_grades.values(), [])) / len(sum(self.teach_grades.values(), []))), 2)
        return self.average_l_rating

    def __str__(self):
        for_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_l_rating}'
        return for_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_l_rating > other.average_l_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return for_reviewer


first_reviewer = Reviewer('Mila', 'Jonas')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Chris', 'Jacoby')
second_reviewer.courses_attached += ['GIT', 'SQL']


first_student = Student('Nastya', 'Fil', 'female')
first_student.courses_in_progress += ['Python', 'GIT']
first_student.finished_courses += ['SQL']

second_student = Student('Kate', 'Rodacheva', 'female')
second_student.courses_in_progress += ['Python', 'GIT']
second_student.finished_courses += []


first_lecturer = Lecturer('Mike', 'Mikelson')
first_lecturer.courses_attached += ['GIT']

second_lecturer = Lecturer('Alex', 'Romanov')
second_lecturer.courses_attached += ['Python']


first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'GIT', 10)
second_reviewer.rate_hw(first_student, 'GIT', 10)
second_reviewer.rate_hw(first_student, 'GIT', 10)
second_reviewer.rate_hw(second_student, 'GIT', 10)
second_reviewer.rate_hw(second_student, 'GIT', 8)


first_student.rate_for_lecturer(first_lecturer, 'GIT', 10)
first_student.rate_for_lecturer(first_lecturer, 'GIT', 10)
first_student.rate_for_lecturer(second_lecturer, 'Python', 9)
first_student.rate_for_lecturer(second_lecturer, 'Python', 9)
second_student.rate_for_lecturer(first_lecturer, 'GIT', 9)
second_student.rate_for_lecturer(first_lecturer, 'GIT', 10)
second_student.rate_for_lecturer(second_lecturer, 'Python', 10)
second_student.rate_for_lecturer(second_lecturer, 'Python', 10)


first_student.average_rate()
second_student.average_rate()
first_lecturer.average_lectors_rate()
second_lecturer.average_lectors_rate()

# print(first_student)
# print(second_student)
# print(first_lecturer)
# print(second_lecturer)
# print(first_reviewer)
# print(second_reviewer)

# print(first_student > second_student)
# print(first_lecturer < second_lecturer)






