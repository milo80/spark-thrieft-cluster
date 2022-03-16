/* Pruebas servidor thrieft <spark-thrift-mono_2022-02-11> */
/* host: 172.23.37.169 */
/* port: 10000 */

/* Verifica base de datos y crea base de datos  */
create database if not exists hive_tst;

/* Crea tabla de prueba "reniecyt_cf" y carga datos desde archivo .csv */
create table if not exists hive_tst.reniecyt_cf(reniecyt string,institucion string,count_proy int)
row format delimited fields terminated by','
escaped by "\\"
lines terminated by '\n'
stored as textfile;

alter table hive_tst.reniecyt_cf set tblproperties ("skip.header.line.count"="1");

load data local inpath '/data_cf/reniecyt_CF.csv' into table hive_tst.reniecyt_cf;


