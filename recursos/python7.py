# Archivo temporal
# * Este archivo tiene que ser subdividido entre los distintos modulos para mas segmentacion.
#! Las funciones deben de ser redefinidas para mayor reusabilidad.

import sqlite3 as sql

"""Comandos:
#? CREATE TABLE -> Crear nueva tabla
#? INSERT INTO ${nameTable} VALUES (...) -> Inserta en la tabla ${nameTable} los valores (...)
#? ... faltan agregar
"""

DB = sql.connect("itbank.db")
"""Abre una conexion con la base de datos. De no existir, la crea."""
def ejecutar(x:str): DB.cursor().executescript(x)
"""Ejecuta una serie de instrucciones SQL en formato script\n
Dentro de esta constante van el resto de funciones.\n 
Ej -> EJECUTAR(createTable('CREADOR', NOMBRE=VARCHAR(90)))"""
CLOSEDB = lambda: DB.close()
"""Cierra la conexion con la base de datos, debe ir al final de EJECUTAR"""

#!👇 Esta funcion debe de convertirse en clase para poder soportar multiples metodos.
#! Dado que el texto inicial no es el mismo para todas las tablas. (leer variable local 'text')
def createTable(nombreTabla:str, **kargs):
    """`*nombreTabla` -> Nombre de la tabla
`**kargs` -> formato: CLAVE = 'VALOR'
    La CLAVE es el nombre de la columna\n
    El VALOR es el tipo de dato esperado.
    """
    keys = []
    values = []

    for key in kargs.keys():
        keys.append(key)
    for value in kargs.values():
        values.append(value)
    
    text=f"""
CREATE TABLE {nombreTabla}(

... id(etc) ...,
"""

    for i in keys:
        k = keys.index(i)
        if k != len(keys) - 1: #* Siempre que no sea la ultima linea, se usaran comas para delimitar.
            text = text + f"""
{i} {values[k]},
"""
        else:
            text = text + f"""
{i} {values[k]}
"""
    ejecutar(text + "\n);")
    CLOSEDB

def insert(nombreTabla:str, nombreColumnas:list, *args):
    """`*nombreTabla` -> Corresponde al nombre de la tabla. Debe de existir previamente,\n
    `*nombreColumnas` -> Corresponde al nombre de la columna. Es donde vamos a introducir valores.\n
    `*args` -> Son los valores. Deben de haber tantos como columnas hayan.
    """
    columnas = ', '.join(nombreColumnas)
    return ejecutar(f'INSERT INTO {nombreTabla}({columnas}) VALUES {args};')

#! Falta crear funciones para:
"""
    1. Mostrar datos por consola✅
    2. Buscar datos en la tabla 
    3. Actualizar datos de la tabla.✅
    4. Borrar datos de la tabla✅
    5. Filtrar la tabla
"""


"1. Mostrar datos por consola"
def displayData(nombreTabla:str, *args):
    """`*nombreTabla` -> Corresponde al nombre de la tabla dentro de la DB. 
    Debe de existir previamente.\n
`*args` -> Corresponde a las columnas elegidas.
    Vamos a recorrer la tupla `args` introduciendo cada elemento separado con una coma,
    segun la sintaxis de ordenes SQL. 
    """
    instruccion = str(f"SELECT {', '.join(args)} from {nombreTabla}")
    tablaSql = DB.execute(instruccion)
    tabla = []
    for fila in tablaSql:
        tabla.append(fila)
    del tablaSql, instruccion
    for fila in tabla:
        for columna in fila:
            print(f"{args[fila.index(columna)]} : {columna}")
        print("\n")
    CLOSEDB

"3. Actualizar datos en la tabla"
def ActualizarFila(nombreTabla:str, condicion:str, **kargs):
    """nombreTabla ...
    condicion -> Debe ser un string\n
`**kargs`-> Valores a reemplazar"""
    columnas = []
    valor = []

    for columna in kargs.keys():
        columnas.append(columna)
    for value in kargs.values():
        valor.append(value)
    
    text=f"""\nUPDATE {nombreTabla}\nSET """
    for columna in columnas:
        k = columnas.index(columna)
        if k != len(columnas) - 1:
            text = text + f"{columna} = {valor[k]},\n"
        else:
            text = text + f"{columna} = {valor[k]}\n"

    text = text + f"\nWHERE {condicion};\n"
    ejecutar(text)

def borrarFila(nombreTabla:str, condicion:str):
    """Este codigo borra las filas (enteras) que cumpla con la condicion
la condicion debe ser un string
    """
    txt=f"""DELETE FROM {nombreTabla} WHERE {condicion}"""
    ejecutar(txt)
    CLOSEDB
if __name__ == "__main__":
    #! Pueden usar esta seccion como pruebas. Lo que esta debajo del __name__ = "__main__"
    #   ! 👆 No se exporta hacia otros archivos.
    pass
