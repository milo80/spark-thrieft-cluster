# Instrucciones de ejecución de pruebas en servidor <spark-thrift-mono_2022-02-11>
# con motor de datos python jaydebeapi
### host: 172.23.37.169
### port: 10000


### Operaciones SQL utilizando python con libreria jaydebapi
### python-3.8 con jar driver [hive-jdbc-2.6.3.jar](https://github.com/timveil/hive-jdbc-uber-jar/releases)

*crea un ambiente virtual o una aplicacion de docker con jupyter notebook
siguiendo las instrucciones en la sección de "instalación".*

Creación de base de datos y tablas internas y externas
```
$python crea_base_datos_y_tablas.py
```

Carga datos a tablas internas y externas
```
$python carga_datos_csv_tabla_int_ext.py
```

Crea tabla y sube datos a base de datos "salsa_lake" 
```
$python carga_datos_csv_tabla_reniecyt.py
```

Ejecuta operaciones CRUD
```
$python modificacion_de_tablas.py
```

Carga tabla en un dataframe de pandas
```
$python hive_a_pandas.py
```

Crea tablas con formato de serializacion AVRO y PARQUET
```
$python formatos_compresion.py
```

### Errores detectados 

**1)**
Al cargar datos a una tabla desde un archivo de texto, en algunas ocaciones
hay que ignorar el renglón del header, con la instrucción :
```
tblproperties ("skip.header.line.count"="1")
```

ya sea a la hora de construir la tabla ó modificandola después con:
```
alter table nombre_tabla set tblproperties ("skip.header.line.count"="1");
```

Esta instrucción no tiene ningún efecto, y la primer fila tendrá 
como valores nos nombres de las columnas.
Al consultar en los glogs de desarrolladores en la red, 
parece ser un problema recurrente con las últimas versionde del driver:
"hive-jdbc-uber-2.6.3.0-235.jar"

**2)**
No soporta renombrar tablas ejemplo:
```
alter table table3 rename to pupulation
```

**3)**
No soporta operaciones de modificacion de tablas con "ALTER"

**4)**
No soporta cambio de nombre o tipo de dato en columnas
```
alter table table3 change col1 id int
```

**5)**
No soporta cambio completo de nombre de columnas
```
Operation not allowed: alter table replace columns(line 1, pos 0)
```

