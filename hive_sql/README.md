# Instrucciones de ejecución de ejemplos en servidor Thrift <spark-thrift-mono_2022-02-11>
# con motor de datos Hive SQL
### host: 172.23.37.169
### port: 10000


### Operaciones SQL utilizando beeline

Creación de base de datos y tablas internas y externas
```
beeline -u 'jdbc:hive2://172.23.37.169:10000' -i crea_base_datos_y_tablas.hql
```

Carga datos a tablas internas y externas
```
beeline -u 'jdbc:hive2://172.23.37.169:10000' -i carga_datos_csv_tabla_int_ext.hql
```

Crea tabla y sube datos a tabla "reniecyt" 
```
beeline -u 'jdbc:hive2://172.23.37.169:10000' -i carga_datos_csv_tabla_reniecyt.hql
```

Elimina bases de datos
```
beeline -u 'jdbc:hive2://172.23.37.169:10000' -i elimina_base_datos.hql
```

Modifica tablas
```
beeline -u 'jdbc:hive2://172.23.37.169:10000' -i modificacion_de_tablas.hql
```


### Errores detectados 

**1)**
Al cargar datos a una tabla desde un archivo de texto, en algunas ocaciones
hay que ignorar el renglón del header, con la instrucción :
tblproperties ("skip.header.line.count"="1")

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
No soporta cambio de nombre o tipo de dato en columnas
```
alter table table3 change col1 id int
```

**4)**
No soporta cambio completo de nombre de columnas
```
Operation not allowed: alter table replace columns(line 1, pos 0)
```
