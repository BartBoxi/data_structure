# Write your MySQL query statement below

with count_of_students as 
(select 
    class,
    count(student) as count_students
from Courses
group by class)
select count_of_students.class
from count_of_students
where count_of_students.count_students >= 5 --requirement was at least 5 
order by count_of_students.class;