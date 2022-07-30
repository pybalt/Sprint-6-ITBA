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
SELECT
	sucursal.branch_name,
	sucursal.branch_id,
	tipo_tarjeta.tipo_tarjeta_nombre,
	count(tarjeta_tipo_marca.tipo_tarjeta_id) as NRO_TARJETAS
	FROM sucursal
		LEFT JOIN cliente
		ON sucursal.branch_id = cliente.branch_id
		LEFT JOIN cliente_cuenta_tipo_tarjeta
		on cliente.customer_id = cliente_cuenta_tipo_tarjeta.customer_id
		LEFT JOIN tarjeta_tipo_marca
		on tarjeta_tipo_marca.tarjeta_tipo_marca_id = cliente_cuenta_tipo_tarjeta.tarjeta_tipo_marca_id
		LEFT JOIN tarjeta
		on tarjeta_tipo_marca.tarjeta_id = tarjeta.tarjeta_id
		LEFT JOIN tipo_tarjeta
		on tipo_tarjeta.tipo_tarjeta_id = tarjeta_tipo_marca.tipo_tarjeta_id
group by sucursal.branch_name;
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

INSERT INTO auditoria_cuenta (old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at)
VALUES
(
1,
2,
3,
4,
5,
6,
7,
8,
9,
datetime('now')
);


CREATE TRIGGER cuenta_BU BEFORE UPDATE on cuenta FOR EACH ROW INSERT INTO auditoria_cuenta
(
old_id, new_id, old_balance, new_balance, 
old_iban, new_iban, old_type, new_type, 
user_action, created_at
)
VALUES
(
old.account_id, new.account_id, old.balance, new.balance,
old.iban, new.iban, old.old_type, new.new_type,
user_action, '2020-10-10') 
)

--6,

CREATE VIEW busquedaDNI as
SELECT customer_id as 'Cliente ID', customer_DNI as 'DNI' FROM cliente

select * from busquedaDNI