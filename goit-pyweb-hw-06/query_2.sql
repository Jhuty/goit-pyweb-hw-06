--Знайти студента із найвищим середнім балом з певного предмета
SELECT Students.Student_name, AVG(Grades.Grade) AS AverageGrade
FROM Students
INNER JOIN Grades ON Students.StudentID = Grades.StudentID
WHERE Grades.SubjectID = 4
GROUP BY Students.StudentID
ORDER BY AverageGrade DESC
LIMIT 1;
