import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10000",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")
#
curs = conn.cursor()
print('Carga datos desde archivo de texto (.csv, .txt) ...')
curs.execute("use python_test")
curs.execute("load data local inpath '/data_cf/table1/table1.csv' into table table1")
print("select * from table1")
curs.close()
print('... ejecucion terminada')
