import mysql.connector # importacion de conector MySQL

#Conexion con Servidor

serverdb = mysql.connector.connect(
  host='localhost', #En caso de ser un servidor externo debemos poner la IP de este y en caso de tener mas de un servidor activo debemos indicar el puerto
  user='root',
  password='',
  database='restaurant'
)

print(serverdb)

mycursor = serverdb.cursor()

mycursor.execute("DROP TABLE cliente")

#chekeo de eliminacion, visualizando las tablas vigentes
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)