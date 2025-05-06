--Cách 1:
select p.product_name, sum(o.unit) as unit
from Products p
join Orders o on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_id, p.product_name
having sum(o.unit) >= 100;

--Cách 2:
with filter as(
    select p.product_name, sum(o.unit) as unit
    from Products p
    left join Orders o on p.product_id = o.product_id
    where month(order_date) = 2 and year(order_date) = 2020
    group by p.product_id
)
select * from filter
where o.unit >= 100;
