# Write your MySQL query statement below

SELECT c.customer_id
FROM Customer c
group by customer_id 
HAVING count(distinct c.product_key) = (select count(distinct p.product_key) FROM Product p);