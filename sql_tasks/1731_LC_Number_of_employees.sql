# Write your MySQL query statement below

with managers_id as (
    select 
        distinct(reports_to) as manager_id,
        count(reports_to) as reports_count
    from 
        Employees
    where reports_to is not null
    group by reports_to
), 
average_age_per_mg as (select
        reports_to as manager_id,
        avg(age) as average_age
        from Employees
        where reports_to is not null
        group by reports_to
    )
select 
    managers_id.manager_id as employee_id,
    e.name as name,
    managers_id.reports_count as reports_count,
    round(average_age_per_mg.average_age,0) as average_age
from managers_id
join average_age_per_mg on managers_id.manager_id = average_age_per_mg.manager_id
join 
Employees e ON managers_id.manager_id = e.employee_id
order by employee_id;