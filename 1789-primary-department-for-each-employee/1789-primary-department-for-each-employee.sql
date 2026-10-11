# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee e
WHERE primary_flag =
    (SELECT MAX(primary_flag) FROM Employee WHERE employee_id = e.employee_id)