-- Solution 1:
select max(salary) as SecondHighestSalary
from Employee 
where salary < (select max(salary) from Employee); 


-- Solution 2:
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
