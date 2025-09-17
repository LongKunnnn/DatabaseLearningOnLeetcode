-- Solution 1:
select l1.Num as ConsecutiveNums
from Logs l1
join Logs l2 on l1.id = l2.id - 1
join Logs l3 on l2.id = l3.id - 1
where l1.num = l2.num
and l2.num = l3.num;

-- Solution 2:
select distinct Num as ConsecutiveNums
from (
    select Num,
    LAG(Num,1) over(order by id) as prev1,
    LAG(Num,2) over(order by id) as prev2
    from Logs
) t
where Num = prev1 and Num = prev2;