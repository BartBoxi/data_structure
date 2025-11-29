# Write your MySQL query statement below
select distinct 
    L.num as ConsecutiveNums
from
    (
        select
            num,
            lag(num,1) over (order by id) as prev_num_1,
            lag(num,2) over (order by id) as prev_num_2
        from
            Logs
    ) as L
where 
    L.num = L.prev_num_1
    and L.num = L.prev_num_2
