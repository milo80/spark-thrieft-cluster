/* Pruebas servidor thrieft */


/* Selecciona base de datos */ 
use hive_tst;

/* Carga datos desde documento .csv a tabla interna*/
load data local inpath '/data_cf/table1/table1.csv' into table table1;
select * from table1;

/* Carga datos desde documento .csv a tabla externa*/
/* Nota: En tablas externas la carga de datos se hace al indicar el path
   en el atributo "location" */
load data local inpath '/data_cf/table1/table1.csv' overwrite into table table2;
select * from table2; 
