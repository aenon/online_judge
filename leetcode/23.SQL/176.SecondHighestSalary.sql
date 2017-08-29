--  176. Second Highest Salary 
--   Write a SQL query to get the second highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+


--  SQL Schema

-- Create table If Not Exists Employee (Id int, Salary int);
-- Truncate table Employee;
-- insert into Employee (Id, Salary) values ('1', '100');
-- insert into Employee (Id, Salary) values ('2', '200');
-- insert into Employee (Id, Salary) values ('3', '300');

# Write your MySQL query statement below

SELECT (
SELECT Salary FROM Employee
GROUP BY Salary
ORDER BY Salary
DESC
LIMIT 1,1) SecondHighestSalary;