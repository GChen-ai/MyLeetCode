CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select ifNUll((select distinct Salary from Employee Order by Salary Desc limit 1 Offset N),null)
  );
END
