--Знайти список студентів у певній групі
SELECT Students.Student_name
FROM Students
INNER JOIN Groups ON Students.GroupID = Groups.GroupID
WHERE Groups.GroupName = 'Group A';
