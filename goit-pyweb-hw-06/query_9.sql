--Знайти список курсів, які відвідує студент.
SELECT DISTINCT Subjects.SubjectName
FROM Subjects
INNER JOIN Grades ON Subjects.SubjectID = Grades.SubjectID
INNER JOIN Students ON Grades.StudentID = Students.StudentID
WHERE Students.Student_name = 'Jennifer Moore';
