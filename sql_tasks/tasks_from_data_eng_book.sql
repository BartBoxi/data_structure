-- task 1 


select 
    id, 
    dense_rank() over (order by score desc) as rank
from Scores
order by score desc;

--