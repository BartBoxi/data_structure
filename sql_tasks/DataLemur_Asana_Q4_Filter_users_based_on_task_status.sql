-- only active users 
-- average of tasks completed per user is 50% 
-- count all tasks per user 
-- count all completed tasks per user 
-- count the average per user 
-- return users with average >= 50% 



select 
    u.user_id,
from 
    users u
inner join 
    (
        select 
            t.task_id, 
            count(t.task_id) as total_tasks,
            count(case when t.task_status = 'Done' then 1 end) as completed_tasks
        from tasks t
        where 
            t.task_completion_date > CURRENT_DATE - interval '1' month
        group by t.user_id
    ) as task_summary
on u.user_id = task_summary.user_id
where 
    u.is_active = true
    and 
    (task_summary.completed_tasks :: decimal / task_summary.total_tasks) > 0.5;    
