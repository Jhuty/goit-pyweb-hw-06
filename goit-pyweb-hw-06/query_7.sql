--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT Students.Student_name, Grades.Grade
FROM Students
INNER JOIN Grades ON Students.StudentID = Grades.StudentID
INNER JOIN Subjects ON Grades.SubjectID = Subjects.SubjectID
INNER JOIN Groups ON Students.GroupID = Groups.GroupID
WHERE Groups.GroupName = 'Group B' AND Subjects.SubjectName = 'school';
