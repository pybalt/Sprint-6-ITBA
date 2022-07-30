-- Cuarta problematica.

--1.
select 
	sucursal.branch_name, 
	sucursal.branch_id,
	count(cliente.customer_name) as numero_de_clientes
		from sucursal
			left join cliente 
				on 
				sucursal.branch_id = cliente.branch_id 
					group by sucursal.branch_id;
--2.
select 
	empleado.branch_id,
	count(empleado.employee_id) / count(cliente.customer_id) 
	as relacion_cliente_empleado
		from sucursal
			inner join cliente
				on
				sucursal.branch_id = cliente.branch_id
			inner join empleado 
				on
				cliente.branch_id = empleado.branch_id
					group by sucursal.branch_id;
--3.
	-- No tengo las tablas correspondientes.
	-- Probar con el siguiente, rellenando los datos:
SELECT
	count(TARJETA.TARJETA_CREDITO),
	SUCURSAL.TIPO_DE_SUCURSAL
		from TARJETA
		inner join SUCURSAL
			on
			TARJETA.COLUMNA1 = SUCURSAL.COLUMNA2
			group by SUCURSAL.SUCURSAL_NAME
				order by TARJETAS_DE_CREDITO, TARJETAS_TIPO;
--4.
select avg(prestamo.loan_total) as promedio_credito,
	sucursal.branch_id,
	sucursal.branch_name
		from prestamo
		inner join cliente
			on
			cliente.customer_id = prestamo.customer_id
		inner join sucursal
			on
			cliente.branch_id = sucursal.branch_id
				group by sucursal.branch_id;
				

--5,

create table auditoria_cuenta (
old_id INTEGER not null,
new_id INTEGER not null,
old_balance INTEGER not null,
new_balance INTEGER not null,
old_iban TEXT not null,
new_iban TEXT not null,
old_type text not null,
new_type text not null,
user_action text not null,
created_at datetime
)


--6,

CREATE VIEW busquedaDNI as
SELECT customer_id as 'Cliente ID', customer_DNI as 'DNI' FROM cliente

select * from busquedaDNI