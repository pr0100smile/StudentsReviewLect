class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ever_grade(self):
        if not self.grades:
            return 'Оценок нет'
        else:
            all_grades = sum(self.grades.values(), [])
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = f'Фамилия студента: {self.surname} \n' \
              f'Имя: {self.name} \n' \
              f'Средняя оценка за домашнее задание: {self.ever_grade()} \n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.ever_grade() < other.ever_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grades(self):
        if not self.grades:
            return 'Оценок нет'
        else:
            all_grades = sum(self.grades.values(), [])
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = f'Фамилия лектора: {self.surname} \n' \
              f'Имя: {self.name} \n' \
              f'Средняя оценка за домашние задания: {self.avg_grades()} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.avg_grades() < other.avg_grades()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                (course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Фамилия эксперта: {self.surname} \nИмя: {self.name} \n'
        return res

def avr_stud_grade(students, course):
    all_grades = []
    for student in students:
        all_grades += student.grades.get(course)
    avrage = sum(all_grades) / len(all_grades)
    return avrage


def avr_lec_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        all_grades += lecturer.grades.get(course)
    midl = sum(all_grades) / len(all_grades)
    return midl


best_student1 = Student('Michael', 'Borisov', 'male')
best_student1.courses_in_progress += ['Python', 'C++', 'Java']
best_student1.finished_courses += ['Swift']

best_student2 = Student('Maria', 'Ivanova', 'female')
best_student2.courses_in_progress += ['Swift', 'HTML', 'Python']
best_student2.finished_courses += ['Java']


lecturer1 = Lecturer('John', 'Kramer')
lecturer2 = Lecturer('Oleg', 'Ivanov')
lecturer1.courses_attached += ['HTML', 'Pascal', 'Python']
lecturer2.courses_attached += ['Swift', 'Java', 'C++']


reviewer1 = Reviewer('Pavel', 'Rybakov')
reviewer2 = Reviewer('Kseniya', 'Markova')
reviewer1.courses_attached += ['Python', 'C++', 'Pascal']
reviewer2.courses_attached += ['Swift', 'HTML', 'Java']


best_student1.rate_lecturer(lecturer1, 'Python', 7)
best_student1.rate_lecturer(lecturer2, 'C++', 9)
best_student1.rate_lecturer(lecturer2, 'Java', 10)

best_student2.rate_lecturer(lecturer2, 'Swift', 9)
best_student2.rate_lecturer(lecturer1, 'HTML', 8)
best_student2.rate_lecturer(lecturer1, 'Python', 10)


reviewer1.rate_hw(best_student1, 'Python', 9)
reviewer1.rate_hw(best_student1, 'C++', 8)
reviewer2.rate_hw(best_student1, 'Java', 10)

reviewer2.rate_hw(best_student2, 'Swift', 6)
reviewer2.rate_hw(best_student2, 'HTML', 8)
reviewer1.rate_hw(best_student2, 'Python', 9)


print(best_student1)
print(best_student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)


if best_student1 < best_student2:
    print(f"Студент {best_student2.name} учится лучше студента {best_student1.name} \n")
else:
    print(f"Студент {best_student1.name} учится лучше студента {best_student2.name} \n")


if lecturer2 < lecturer1:
    print(f"Лектор {lecturer1.name} лучше лектора {lecturer2.name} \n")
else:
    print(f"Лектор {lecturer2.name} лучше лектора {lecturer1.name} \n")

students_all = [best_student1, best_student2]
lecturers_all = [lecturer1, lecturer2]


def av_hw_students(students, course):
    all_grades_students = []
    for student in students:
        all_grades_students += student.grades.get(course)
    hw_grade = round(sum(all_grades_students) / len(all_grades_students), 2)
    return hw_grade


def av_hw_lecturers(lecturers, course):
    all_grades_lecturers = []
    for lecture in lecturers:
        all_grades_lecturers += lecture.grades.get(course, [])
    hw_grades = round(sum(all_grades_lecturers) / len(all_grades_lecturers), 2)
    return hw_grades


print('Cредняя оценка за домашние задания по всем студентам: ', av_hw_students(students_all, 'Python'))
print('\nCредняя оценка за лекции всех лекторов: ', av_hw_lecturers(lecturers_all, 'Java'))