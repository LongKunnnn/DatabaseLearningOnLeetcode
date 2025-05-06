select s.student_id, s.student_name, sub.subject_name,
ifnull(count(e.student_id),0) as attended_exams
from Students s
cross join Subjects sub
left join Examinations e on e.student_id = s.student_id and e.subject_name = sub.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, s.student_name;
