-- Список курсів, які певному студенту читає певний викладач
SELECT DISTINCT Subjects.SubjectName
FROM Subjects
INNER JOIN Grades ON Subjects.SubjectID = Grades.SubjectID
INNER JOIN Students ON Grades.StudentID = Students.StudentID
INNER JOIN Teachers ON Subjects.TeacherID = Teachers.TeacherID
WHERE Students.Student_name = 'Lisa Graves' AND Teachers.teacher_name = 'Christopher Olson';
