# Write your MySQL query statement below

with cumulative_weight as (
    select 
        turn, 
        person_id,
        person_name,
        weight,
        sum(weight) over (order by turn) as total_weight 
    from Queue
)
select 
    person_name
from cumulative_weight
where total_weight <= 1000
order by turn desc
limit 1;
