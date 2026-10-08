# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1 
WHERE EXISTS (SELECT 1 FROM Weather W2 where DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature);

