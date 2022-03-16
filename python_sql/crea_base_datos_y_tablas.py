import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10000",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")
#
curs = conn.cursor()
print('Creacion de base de datos y tabas ...')

curs.execute("create database if not exists python_test")
curs.execute("use python_test")
Q1 = "create table if not exists int_table"\
     "(col1 int,col2 array<string>,col3 string,col4 int) "\
     "row format delimited fields terminated by',' "\
     "collection items terminated by':' "\
     "lines terminated by'\n' "\
     "stored as textfile"
curs.execute(Q1)
Q2 = "create external table if not exists ext_table"\
     "(col1 int,col2 array<string>,col3 string,col4 int) "\
     "row format delimited fields terminated by',' "\
     "collection items terminated by':' "\
     "lines terminated by'\n' "\
     "stored as textfile "\
     "location '/data_cf/table1/'"
curs.execute(Q2)
print(curs.execute("show tables"))
curs.close()
print('... ejecucion terminada')
