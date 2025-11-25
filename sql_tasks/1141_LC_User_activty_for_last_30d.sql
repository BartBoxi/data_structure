# Write your MySQL query statement below

select 
    activity_date as day,
    count(distinct(user_id)) as active_users
from 
    Activity
where 
    activity_date >= ('2019-07-28'- interval 30 day) and activity_date < '2019-07-28' -- here important is to use proper inclusion of the dates 
    -- if we use <= '2019-07-28' then we will include also the last day
    -- if we use < '2019-07-28' then we will not include the last day
group by day
order by day asc;


