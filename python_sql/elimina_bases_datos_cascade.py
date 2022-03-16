import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10000",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")
#                          "./drivers_jar/hive-jdbc-uber-2.4.0.0-169.jar")
#
curs = conn.cursor()
print('Elimina bases de datos python_test, salsa_lake ...')

curs.execute("drop database if exists python_test cascade")
curs.execute("drop database if exists salsa_lake cascade")
curs.close()
print('... ejecucion terminada')
