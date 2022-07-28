CREATE TABLE 'tipo_cuenta'(
	'tipo_cuenta_id' INTEGER not NULL,
	'tipo_cuenta_nombre' TEXT nor NULL,
	PRIMARY KEY('tipo_cuenta_id' AUTOINCREMENT)
);

CREATE TABLE 'tipo_tarjeta'(
	'tipo_tarjeta_id' INTEGER not NULL,
	'tipo_tarjeta_nombre' TEXT nor NULL,
	PRIMARY KEY('tipo_tarjeta_id' AUTOINCREMENT)
);

CREATE TABLE 'marca_tarjeta'(
	'marca_tarjeta_id' INTEGER not NULL,
	'marca_tarjeta_nombre' TEXT nor NULL,
	PRIMARY KEY('marca_tarjeta_id' AUTOINCREMENT)
);

CREATE TABLE `tarjeta` (
  `tarjeta_id` INTEGER NOT NULL,
  `tarjeta_numero` varchar(255),
  `tarjeta_cvv` varchar(255),
  `tarjeta_fecha_otorgamiento` varchar(255),
  `tarjeta_fecha_expiracion` varchar(255),
  PRIMARY KEY (`tarjeta_id` AUTOINCREMENT)
)

INSERT INTO tipo_cliente (tipo_cliente_nombre)
VALUES('BLACK');

INSERT INTO tipo_cuenta (tipo_cuenta_nombre)
VALUES
('CAJA DE AHORRO EN PESOS'),
('CAJA DE AHORRO EN DOLARES'),
('CUENTA CORRIENTE');

CREATE TABLE tarjeta_tipo_marca(
	tarjeta_tipo_marca_id INTEGER not NULL,
	tarjeta_id INTEGER not null REFERENCES tarjeta(tarjeta_id),
	tipo_tarjeta_id INTEGER not null REFERENCES tipo_tarjeta(tipo_tarjeta_id),
	marca_tarjeta_id INTEGER not null REFERENCES marca_tarjeta(marca_tarjeta_id),
	PRIMARY KEY('tarjeta_tipo_marca_id' AUTOINCREMENT)
);
create TABLE cliente_cuenta_tipo_tarjeta(
	cliente_cuenta_tipo_tarjeta_id INTEGER not NULL,
	customer_id INTEGER not NULL,
	tipo_cliente_id INTEGER not null,
	caja_pesos INTEGER not NULL
	caja_dolares INTEGER not NULL
	caja_ahorro INTEGER not NULL
	tarjeta_tipo_marca_id INTEGER not NULL
	PRIMARY KEY(cliente_cuenta_tipo_tarjeta_id, AUTOINCREMENT)
);
SELECT DISTINCT customer_id, tarjeta_tipo_marca_id FROM cliente_cuenta_tipo_tarjeta;

CREATE TABLE direccion(
	direccion_id INTEGER not NULL,
	direccion_calle TEXT not NULL,
	direccion_numero_calle INTEGER not NULL,
	direccion_ciudad TEXT not NULL,
	direccion_provincia TEXT not NULL,
	direccion_pais TEXT not null,
	PRIMARY kEY(direccion_id AUTOINCREMENT)
);
INSERT INTO direccion (direccion_calle, direccion_numero_calle, direccion_ciudad, direccion_provincia, direccion_pais)
VALUES

SELECT * FROM `cliente`  
ORDER BY `cliente`.`customer_DNI` DESC

SELECT *,date('now') as fecha,
strftime('%Y', date('now')) - strftime('%Y', date(dob)) as EDAD
--,strftime('%Y', date('now')) as ano
--,strftime('%m', date('now')) as mes
--,strftime('%d', date('now')) as dia
FROM cliente
ORDER BY `cliente`.`customer_DNI` DESC

SELECT *,date('now') as fecha,
strftime('%Y', date('now')) - strftime('%Y', date(dob)) as EDAD
--,strftime('%Y', date('now')) as ano
--,strftime('%m', date('now')) as mes
--,strftime('%d', date('now')) as dia
FROM cliente WHERE EDAD>40
ORDER by customer_DNI asc


SELECT *, date('now') as fecha,
strftime('%Y', date('now')) - strftime('%Y', date(dob)) as EDAD
customer_name FROM cliente WHERE customer_name = 'Tyler' or customer_name = 'Anne'

SELECT *, date('now') as fecha,
strftime('%Y', date('now')) - strftime('%Y', date(dob)) as EDAD
from cliente WHERE customer_name = 'Tyler' or customer_name = 'Anne' ORDER by edad asc
SELECT *, date('now') as fecha,
strftime('%Y', date('now')) - strftime('%Y', date(dob)) as EDAD
from cliente WHERE customer_name = 'Tyler' or customer_name = 'Anne' ORDER by edad asc
