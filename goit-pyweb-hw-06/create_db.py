import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()


#Создание таблицы групп
cursor.execute('''CREATE TABLE IF NOT EXISTS Groups (
    GroupID INTEGER PRIMARY KEY,
    GroupName TEXT
);''')


#создание таблицы преподавателей
cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers (
    TeacherID INTEGER PRIMARY KEY,
    teacher_name TEXT
);''')


#Создание таблицы предметов
cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
    SubjectID INTEGER PRIMARY KEY,
    SubjectName TEXT,
    TeacherID INTEGER,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);''')


 #Создание таблицы студентов
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    Student_name TEXT,
    GroupID INTEGER,
    FOREIGN KEY (GroupID) REFERENCES Groups(GroupID)
);''')


#Создание таблицы оценок
cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
    GradeID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    SubjectID INTEGER,
    Grade REAL,
    GradeDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);''')


conn.commit()
conn.close()