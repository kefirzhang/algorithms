select D.Name as Department,E.name as Employee,E.Salary as Salary from Employee E join Department D on  E.DepartmentId=D.Id where  (DepartmentId,Salary) in (select DepartmentId,max(Salary) as Salary from Employee group  by DepartmentId)
