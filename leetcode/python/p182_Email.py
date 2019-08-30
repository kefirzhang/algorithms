# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
#
# SELECT Email from (SELECT count(*) as num,Email FROM `Person` group by Email) as t WHERE num > 1