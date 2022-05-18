import mysql.connector # importacion de conector MySQL

#Conexion con Servidor

serverdb = mysql.connector.connect(
  host='localhost', #En caso de ser un servidor externo debemos poner la IP de este y en caso de tener mas de un servidor activo debemos indicar el puerto
  user='root',
  password=''
)

print(serverdb)

mycursor = serverdb.cursor()

mycursor.execute("CREATE DATABASE restaurant")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)