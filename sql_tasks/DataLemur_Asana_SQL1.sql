with monthly_avg as (
    select 
        date_part('month', create_date)::int as mth, 
        avg(complete_date - create_date)::float as avg_completion_time
    from tasks
    where 
        date_part('month', create_date) = date_part('month', complete_date) and 
        date_part('year', create_date) = date_part('year', complete_date)
    group by mth
)
select * from monthly_avg
order by mth;