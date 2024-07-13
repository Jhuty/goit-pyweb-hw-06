--Знайти середній бал у групах з певного предмета.
SELECT Groups.GroupName, AVG(Grades.Grade) AS AverageGrade
FROM Groups
INNER JOIN Students ON Groups.GroupID = Students.GroupID
INNER JOIN Grades ON Students.StudentID = Grades.StudentID
WHERE Grades.SubjectID = 3
GROUP BY Groups.GroupID;
