-- Tercer problematica

-- 1.
select 
	* 
		from cuenta 
			where balance < 0 
				order by balance;
-- 2.
select 
	customer_name,
	customer_surname,
	round(
		(JULIANDAY('now') - JULIANDAY(dob))/365.25
		) 
	as años
		from cliente 
			where customer_surname 
				like '%z';
-- 3.
select 
	date(dob) as fechanacimiento,
	date('now'), 
	round(
		(JULIANDAY('now') - JULIANDAY(dob))/365.25
		) 
	as años
		from cliente 
			where customer_name = 'Brendan' 
				order by años desc;
-- 4.
select 
	* 
		from prestamo
			where (prestamo.loan_total > 8000000 
			or prestamo.loan_type = 'PRENDARIO')
				ORDER BY loan_total;
-- 5. 
select 
	* 
		from prestamo
			where loan_total > (
					select avg(loan_total) from prestamo
								);
-- 6.
select 
* 
	from cliente 
		where
			round((JULIANDAY('now') - JULIANDAY(dob))/365.25) < 50;
-- 7.
select 
	* 
	from cuenta 
		where balance > 800000 
			order by rowid limit 5;
-- 8.
select 
	* 
		from prestamo
			where 
				loan_date LIKE '____%-04-%__' 
				or loan_date LIKE '____%-06-%__'
				or loan_date LIKE'____%-08-%__'
					order by loan_total;
-- 9.
select 
	sum(loan_total) as loan_total_accu,
	loan_type
		from prestamo
			group by loan_type;