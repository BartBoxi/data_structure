# Write your MySQL query statement below

select 
    s.product_id,
    s.year as first_year, 
    s.quantity as quantity,
    s.price
from 
    Sales s
JOIN (
    select 
        product_id, 
        min(year) as min_year
    from Sales
    group by product_id
) min_years on s.product_id = min_years.product_id
and s.year = min_years.min_year
order by s.product_id;

