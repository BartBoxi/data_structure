# Write your MySQL query statement below

with first_order as
(select 
customer_id, 
min(order_date) as min_date
from Delivery
group by customer_id
order by customer_id)

select 
    round(((count(case when first_order.min_date = Delivery.customer_pref_delivery_date then 1 end)/ count(distinct first_order.customer_id))* 100.0),2) as immediate_percentage

from
    Delivery 
left join
  first_order 
on Delivery.customer_id = first_order.customer_id;

