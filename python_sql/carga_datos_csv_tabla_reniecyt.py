import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10000",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")
#                          "./drivers_jar/hive-jdbc-uber-2.4.0.0-169.jar")
#
curs = conn.cursor()
print('Creacion de base de datos salsa_lake ...')

curs.execute("create database if not exists python_test")
curs.execute("use python_test")
Q1 = "create table if not exists reniecyt_cf"\
     "(reniecyt string,institucion string,count_proy int) "\
     "row format delimited fields terminated by ',' "\
     "lines terminated by '\n' "\
     "stored as textfile"
curs.execute(Q1)
curs.execute("alter table reniecyt_cf set tblproperties ('skip.header.line.count'='1')")

Q2 = "load data local inpath '/data_cf/reniecyt_CF.csv' "\
     "overwrite into table reniecyt_cf"
curs.execute(Q2)
curs.close()
print('... ejecucion terminada')
