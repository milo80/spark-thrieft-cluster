import pandas as pd
import jaydebeapi


conn = jaydebeapi.connect("org.apache.hive.jdbc.HiveDriver",
                          "jdbc:hive2://172.23.37.169:10001",
                          ["dbt", "dbt"],
                          "./drivers_jar/hive-jdbc-uber-2.6.3.0-235.jar")

curs = conn.cursor()
curs.execute("create database if not exists python_test")
curs.execute("use python_test")
QRY = "create table if not exists persona_fisica"\
      "(id int,cvu string,nombre string,rfc string,nivel_sni string) "\
      "row format delimited fields terminated by ',' "\
      "lines terminated by '\n' "\
      "stored as textfile"
curs.execute(QRY)
QRY = "load data local inpath '/opt/spark/bin/spark-warehouse/persona_fisica/persona_fisica_cf.csv' "\
      "overwrite into table persona_fisica"
curs.execute(QRY)
curs.execute("select * from persona_fisica")

cols = ['id', 'cvu', 'nombre', 'rfc', 'nivel_sni']
df = pd.DataFrame(curs.fetchall(), columns=cols)
print(df.head(10))
curs.close()
print('ejecucion terminada')
