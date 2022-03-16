-- Pruebas servidor thrieft <spark-thrift-mono_2022-02-11>  
-- host: 172.23.37.169  
-- port: 10000  

-- Verifica base de datos y crea base de datos   
create database if not exists hive_tst;
use hive_tst;

-- Crea tabla de prueba "reniecyt_cf" y carga datos desde archivo .csv  
create table if not exists reniecyt_cf(reniecyt string,institucion string,count_proy int)
row format delimited fields terminated by','
escaped by "\\"
lines terminated by '\n'
stored as textfile;

load data local inpath '/data_cf/reniecyt_CF.csv' overwrite into table reniecyt_cf;


-- Modifica nombre de tabla  
-- Driver no soporta renombrar tablas  
-- alter table reniecyt_cf rename to reniecyt;  

-- Modifica nombre de columnas  
-- Driver no soporta renombrar columnas con instrucción CHANGE  
-- alter table reniecyt_cf change count_proy counts string;  

-- Reemplaza todas las columnas  
-- Driver no soporta reemplazar las columnas con instrucción REPLACE COLUMNS  
-- alter table reniecyt_cf replace columns(id_r int,institucion string, conteo int);  

-- Ingresa datos a tablas  
insert into table reniecyt_cf values (11101,"UNAM INGENIERIA",2);  

-- Consultas con filtro  
select * from reniecyt_cf where count_proy<3;


