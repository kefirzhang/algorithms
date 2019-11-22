select 
	d.name as Department,e1.Name as Employee,e1.Salary as Salary
from 
	Employee as e1 
	join Department as d on e1.DepartmentId=d.Id 
where 
	3	>
(select count(distinct(e2.Salary)) from Employee as e2 where e2.Salary > e1.Salary and e2.DepartmentId=e1.DepartmentId )

