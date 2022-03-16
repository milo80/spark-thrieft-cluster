/* Pruebas servidor thrieft */


/* Crea base de datos y crea tablas */ 
create database if not exists hive_tst;
use hive_tst;

/* Crea tabla interna */
create table if not exists table1(col1 int,col2 array<string>,col3 string,col4 int) 
row format delimited fields terminated by','
collection items terminated by':'
lines terminated by'\n'
stored as textfile;

/* Crea tabla externa */
create external table if not exists table2(col1 int,col2 array<string>,col3 string,col4 int)
row format delimited fields terminated by','
collection items terminated by':'
lines terminated by'\n'
stored as textfile
location '/data_cf/table1/';
