--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT Teachers.teacher_name, AVG(Grades.Grade) AS AverageGrade
FROM Teachers
INNER JOIN Subjects ON Teachers.TeacherID = Subjects.TeacherID
INNER JOIN Grades ON Subjects.SubjectID = Grades.SubjectID
WHERE Teachers.teacher_name = 'Joshua Campbell'
GROUP BY Teachers.teacher_name;
