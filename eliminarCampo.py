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
rut = input("Ingrese el RUT que desea eliminar: ")
sql= "DELETE FROM "+database+" WHERE rut = '"+rut+"'"

#Ejecucion de la eliminacion de campos
mycursor.execute(sql)

serverdb.commit()

#Cantidad de registros eliminados
print(mycursor.rowcount, "Registro(s) Eliminado(s)")