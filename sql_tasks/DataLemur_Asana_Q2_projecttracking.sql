-- project id 
-- count of all the tasks
-- count of completed tasks - task_status -> "Done"
-- count of percentage completed / total tasks 

select 
    p.project_name,
    100 * count(case when t.task_status = 'Done' then 1 end) / count(t.task_id) as percentage_completed
from projects p 
join tasks t 
on p.project_id = t.project_id
group by p.project_id;

    