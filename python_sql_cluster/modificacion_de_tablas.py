import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10001",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")
#
curs = conn.cursor()
curs.execute("create database if not exists python_test")
curs.execute("use python_test")

print('Ejecución de operaciones CRUD ...')
print("Crea tabla y carga datos ...")
Q1 = "create table if not exists reniecyt_cf"\
     "(reniecyt string,institucion string,count_proy int) "\
     "row format delimited fields terminated by ',' "\
     "lines terminated by '\n' "\
     "stored as textfile"
curs.execute(Q1)
Q2 = "load data local inpath '/opt/spark/bin/spark-warehouse/reniecyt_CF.csv' "\
     "overwrite into table reniecyt_cf"
curs.execute(Q2)

QRY = "desc reniecyt_cf"
curs.execute(QRY)
res = curs.fetchmany(5)
print(res)
#
print("Modifica nombre de tabla ...")
# Driver no soporta renombrar tablas
#curs.execute("ALTER TABLE reniecyt_cf RENAME TO reniecyt")
#res = curs.fetchall()
#print(res)
#
print("Modifica nombre de columnas ...")
# Driver no soporta renombrar columnas con instrucción CHANGE
#curs.execute("ALTER TABLE reniecyt_cf CHANGE count_proy count int")
#res = curs.fetchall()
#print(res)

print("Reemplaza todas las columnas")
# Driver no soporta reemplazar las columnas con instrucción REPLACE COLUMNS
#QRY = "ALTER TABLE reniecyt_cf REPLACE COLUMNS"\
#      "(id_ren int,institucion_nombre string,conteo int)"
#curs.execute(QRY)
#res = curs.fetchall()
#print(res)

print("Ingresa datos a tabla")
QRY = "INSERT INTO TABLE reniecyt_cf "\
      "VALUES (101010,'UNAM INGENIERIA',2)"
curs.execute(QRY)
res = curs.fetchall()
print(res)
#

print("Consultas con filtro")
QRY = "SELECT * FROM reniecyt_cf WHERE count_proy<3"
curs.execute(QRY)
res = curs.fetchall()
print(res)

curs.close()
print('\n\n... Pruebas ejecutadas exitosamente')
