--1

SELECT * 
FROM cliente
INNER JOIN sucursal
on cliente.branch_id = sucursal.branch_id
ORDER BY branch_id desc

--2