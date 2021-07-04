class Student:
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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teach_grades = {}
        self.average_rating = 0

    def average_lectors_rate(self):
        self.average_rating += round((sum(sum(self.teach_grades.values(), [])) / len(sum(self.teach_grades.values(), []))), 2)
        return self.average_rating

    def __str__(self):
        for_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_lectors_rating}'
        return for_lecturer

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_rating > other.average_rating


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


cool_reviewer = Reviewer('Mila', 'Jonas')
cool_reviewer.courses_attached += ['Python']

best_student = Student('Nastya', 'Fil', 'female')
best_student.courses_in_progress += ['Python', 'SQL']
best_student.finished_courses += ['GIT']
best_student.grades["Python"] = [10, 10, 10]
best_student.grades["SQL"] = [9, 9, 10]

cool_lecturer = Lecturer('Mike', 'Mikelson')
cool_lecturer.courses_attached += ['GIT']

cool_reviewer.rate_hw(best_student, 'Python', 10)
# print(f'Оценка студенту {best_student.name} {best_student.surname}: {best_student.grades}')

best_student.rate_for_lecturer(cool_lecturer, 'GIT', 10)
# print(f'Оценка лектору {cool_lecturer.name} {cool_lecturer.surname} : {cool_lecturer.teach_grades}')
cool_lecturer.teach_grades["Python"] = [10, 8, 10]
cool_lecturer.teach_grades["GIT"] = [10, 10, 10]

best_student.average_rate()
cool_lecturer.average_lectors_rate()

# print(cool_reviewer)
# print(cool_lecturer)
# print(best_student)

print(cool_lecturer.average_rating < best_student.average_rating)



