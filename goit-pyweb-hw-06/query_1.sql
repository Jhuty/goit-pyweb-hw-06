--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT Students.Student_name, AVG(Grades.Grade) AS AverageGrade
FROM Students
INNER JOIN Grades ON Students.StudentID = Grades.StudentID
GROUP BY Students.StudentID
ORDER BY AverageGrade DESC
LIMIT 5;
