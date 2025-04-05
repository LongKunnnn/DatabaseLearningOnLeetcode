select email from Person
group by email
having (select count (*) from Person p where p.email = Person.email ) > 1;