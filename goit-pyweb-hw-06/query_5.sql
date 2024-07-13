--Знайти які курси читає певний викладач.
SELECT DISTINCT Subjects.SubjectName
FROM Subjects
INNER JOIN Teachers ON Subjects.TeacherID = Teachers.TeacherID
WHERE Teachers.teacher_name = 'Joshua Campbell';