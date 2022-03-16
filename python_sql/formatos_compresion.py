import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10000",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")

curs = conn.cursor()

print('Creacion de tabla con compressión parquet')
curs.execute("create database if not exists python_test")
curs.execute("use python_test")

# Creacion de tabla temporal
QRY = "create external table if not exists tmp_csv_pf"\
      "(id int,cvu string,nombre string,rfc string,nivel_sni string) "\
      "row format delimited fields terminated by ',' "\
      "lines terminated by '\n' "\
      "stored as textfile "\
      "location '/data_cf/persona_fisica/'"
curs.execute(QRY)

# Creacion de tabla parquet
print("Creacion de tabla con formato parquet")
QRY = "create table if not exists parquet_pf"\
      "(id int,cvu string,nombre string,rfc string,nivel_sni string) "\
      "stored as parquet"
curs.execute(QRY)
# Carga datos a tabla parquet
QRY = "insert into table parquet_pf select * from tmp_csv_pf"
curs.execute(QRY)

print("Creacion de tabla con formato ORC")
QRY = "create table if not exists orc_pf"\
      "(id int,cvu string,nombre string,rfc string,nivel_sni string) "\
      "stored as orc"
curs.execute(QRY)
# Carga datos a tabla parquet
QRY = "insert into table orc_pf select * from tmp_csv_pf"
curs.execute(QRY)

curs.execute("show tables")
res = curs.fetchall()
print("tablas creadas ...\n", res)


curs.close()
print('ejecucion terminada')
