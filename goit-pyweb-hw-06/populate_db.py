import sqlite3
from faker import Faker
import random


conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Инициализация faker для генерации случайных данных
fake = Faker()

# Генерация данных для таблицы групп
groups = [(1, "Group A"), (2, "Group B"), (3, "Group C")]  # 3 группы
cursor.executemany('INSERT INTO Groups (GroupID, GroupName) VALUES (?, ?);', groups)

# Генерация данных для таблицы преподавателей
teachers = [(i, fake.name()) for i in range(1, random.randint(3, 6))]  # 3-5 преподавателей
cursor.executemany('INSERT INTO Teachers (TeacherID, teacher_name) VALUES (?, ?);', teachers)

# Генерация данных для таблицы предметов со случ. назнач. преподавателем
subjects = []
for i in range(1, random.randint(5, 9)):  # 5-8 предметов
    teacher_id = random.randint(1, len(teachers))
    subjects.append((i, fake.word(), teacher_id))

cursor.executemany('INSERT INTO Subjects (SubjectID, SubjectName, TeacherID) VALUES (?, ?, ?);', subjects)

# Генерация данных для таблицы студентов
students = []
for i in range(1, random.randint(30, 51)):  # 30-50 студентов
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    students.append((i, student_name, group_id))

cursor.executemany('INSERT INTO Students (StudentID, Student_name, GroupID) VALUES (?, ?, ?);', students)

# Генерация данных для таблицы оценок
grades = []
for student_id in range(1, len(students) + 1):
    for subject_id in range(1, len(subjects) + 1):
        num_grades = random.randint(5, 20)  # случайное кол-во оценок, до 20 для каждого студента на каждый предмет
        for _ in range(num_grades):
            grade = round(random.uniform(60, 100), 2)  # оценки от 60 до 100
            grade_date = fake.date_between(start_date='-1y', end_date='today')
            grades.append((None, student_id, subject_id, grade, grade_date))

cursor.executemany('INSERT INTO Grades (GradeID, StudentID, SubjectID, Grade, GradeDate) VALUES (?, ?, ?, ?, ?);', grades)


conn.commit()
conn.close()

print("Данные успешно сгенерированы и записаны в БД.")
