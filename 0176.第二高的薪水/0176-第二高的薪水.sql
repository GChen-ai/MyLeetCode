# Write your MySQL query statement below
select ifNull((select distinct Salary from Employee Order by Salary Desc limit 1,1),null) as SecondHighestSalary;