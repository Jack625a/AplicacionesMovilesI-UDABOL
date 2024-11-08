import sqlite3 #Importacion de dependencias de sqlite

#Paso 1. Crear o conectar a una base de datos
conexion=sqlite3.connect('datos.db')

#Paso 2. Crear un cursor para manejar las consultas SQL
cursor=conexion.cursor()
#nombre=input("Ingrese su nombre: ")
#edad=int(input("Ingrese su edad: "))
#celular=int(input("Ingrese su celular: "))
#Paso 3. Ejecutar la consulta SQL
cursor.execute("SELECT * FROM usuarios")
#Paso 3.1. PARA CONSULTAS SELECT - RECUPERAR LOS DATOS
usuarios=cursor.fetchall()
#Mostrar los datos
for usuario in usuarios:
    print(usuario[1],"Edad:",usuario[2],"años")


#Paso 4. Enviar los cambios a la Base de Datos
conexion.commit()
