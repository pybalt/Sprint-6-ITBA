
import sqlite3 as sql


OPEN_DB = sql.connect("itbank.db")

CLOSEDB = lambda: OPEN_DB.close()