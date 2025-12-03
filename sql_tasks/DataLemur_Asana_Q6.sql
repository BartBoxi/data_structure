-- As a data analyst at Asana, you have been tasked to filter thorough the customer records database 
--to find customers whose emails contain 'asana'. Filter only customers who registered in the year 2021.

select 
    customer_id, 
    name, 
    email,
    registration_date
from 
    customers
where 
    email like '%asana%' and 
    registration_date >= '2021-01-01' and 
    registration_date < '2022-01-01';


-- alternative solution 

select * 
from customers 
where email like '%asana%' and date_part('year', registration_date) = 2021;
