class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_for_lecturer(self, lecturer, course, lecturer_grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.teach_grades:
                lecturer.teach_grades[course] += [lecturer_grade]
            else:
                lecturer.teach_grades[course] = [lecturer_grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teach_grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


cool_reviewer = Reviewer('Mila', 'Jonas')
cool_reviewer.courses_attached += ['Python']

best_student = Student('Nastya', 'Fil', 'female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']

cool_lecturer = Lecturer('Mike', 'Mikelson')
cool_lecturer.courses_attached += ['GIT']

cool_reviewer.rate_hw(best_student, 'Python', '10')
print(f'Оценка студенту {best_student.name} {best_student.surname}: {best_student.grades}')

best_student.rate_for_lecturer(cool_lecturer, 'GIT', '10')
print(f'Оценка лектору {cool_lecturer.name} {cool_lecturer.surname} : {cool_lecturer.teach_grades}'
      )


