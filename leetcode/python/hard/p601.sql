select distinct s1.* from stadium s1,stadium s2,stadium s3
where
    (
            (datediff(s1.visit_date,s2.visit_date)=-1 and datediff(s1.visit_date,s3.visit_date)=-2)
        or
            (datediff(s1.visit_date,s2.visit_date)=1 and datediff(s1.visit_date,s3.visit_date)=-1)
        or
            (datediff(s1.visit_date,s2.visit_date)=1 and datediff(s1.visit_date,s3.visit_date)=2)
    )

and s1.people >=100 and s2.people >=100 and s3.people >=100 order by id asc