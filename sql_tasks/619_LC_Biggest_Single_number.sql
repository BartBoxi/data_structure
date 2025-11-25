# Write your MySQL query statement below

-- first, easiest solution that came to my mind but not the best one.
with single_numbers as (
    select 
        num, 
        count(num) as count
    from
        MyNumbers
    group by num
    order by num desc
)
select max(single_numbers.num) as num
from single_numbers
where single_numbers.count = 1;


--- below I was trying to find even more efficient solution

select max(num) as num
from (
    select num 
    from MyNumbers
    group by num
    having count(num) = 1
) as unique_nums;