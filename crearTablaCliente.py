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

#Crear base de dato cliente
mycursor.execute("CREATE TABLE cliente (nombre VARCHAR(100), apellido VARCHAR(150), rut VARCHAR(10), direccion VARCHAR(300))")

#chekeo de crecion, visualizando las tablas creadas
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)