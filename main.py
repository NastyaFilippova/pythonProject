class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.teach_grades = {}

    def rate_teaching(self, student, course, teach_grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.teach_grades:
                self.teach_grades[course] += [teach_grade]
            else:
                self.teach_grades[course] = [teach_grade]
        else:
            return 'Ошибка'


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

cool_lecturer = Lecturer('Mike', 'Mikelson')
cool_lecturer.courses_attached += ['GIT']

new_student = Student('Nelly', 'Sidorova', 'female')
new_student.courses_in_progress += ['GIT']

cool_reviewer.rate_hw(best_student, 'Python', '10')
print(f'Оценка студенту {best_student.name} {best_student.surname}: {best_student.grades}')

cool_lecturer.rate_teaching(new_student, 'GIT', '10')
print(f'Оценка преподавателю {cool_lecturer.name} {cool_lecturer.surname} от студента {new_student.name} {new_student.surname}: {cool_lecturer.teach_grades}'
      )


