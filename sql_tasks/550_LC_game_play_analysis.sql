# Write your MySQL query statement below

with first_login as (
    select 
        player_id, 
        min(event_date) as first_login
    from Activity
    group by player_id
),

second_login as (
select 
    a.player_id as player_id, 
    a.event_date as second_login
from Activity a
join first_login f
    on a.player_id = f.player_id
where 
    a.event_date = f.first_login + interval 1 day)

select 
   round(count(distinct s.player_id) / count(distinct a.player_id),2) as fraction
from Activity a
left join second_login s
on s.player_id = a.player_id;