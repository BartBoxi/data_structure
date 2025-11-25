# Write your MySQL query statement below

with count_of_products as (
    select 
        count(distinct(product_key)) as number_of_products
    from Product
), 
count_of_products_per_cx as (
select
    customer_id, 
    count(distinct(product_key)) as number_of_prod
from Customer
group by customer_id
)
select 
    count_of_products_per_cx.customer_id
from 
    count_of_products_per_cx
join 
    count_of_products
where 
    count_of_products_per_cx.number_of_prod = count_of_products.number_of_products
group by count_of_products_per_cx.customer_id
order by count_of_products_per_cx.customer_id;

