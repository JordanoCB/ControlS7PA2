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

#Lista de tablas vigentes
print("Lista de Bases de datos")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

#Ingreso manual de la tabla donde queremos realizar la insercion
database = input("Ingrese el nombre de la base de datos:")
sql= "INSERT INTO "+database+" (nombre, apellido, rut, direccion) VALUES (%s, %s, %s, %s)"

#Campos digitados por pantalla de los campos solicitados por la tabla
nombre = input("Ingrese el Nombre: ")
apellido = input("Ingrese el Apellido: ")
rut = input("Ingrese el RUT: ")
direccion = input("Ingrese la direccion: ")
val = (nombre, apellido, rut, direccion)

#Ejecucion de la insercion de campos
mycursor.execute(sql, val)

serverdb.commit()

#Cantidad de registros insertados
print(mycursor.rowcount, "Registro Insertado")