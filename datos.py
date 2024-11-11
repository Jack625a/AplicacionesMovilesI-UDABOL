import sqlite3 #Importacion de dependencias de sqlite

#Paso 1. Crear o conectar a una base de datos
conexion=sqlite3.connect('datos.db')

#Paso 2. Crear un cursor para manejar las consultas SQL
cursor=conexion.cursor()
#nombre=input("Ingrese su nombre: ")
#edad=int(input("Ingrese su edad: "))
#celular=int(input("Ingrese su celular: "))
#Paso 3. Ejecutar la consulta SQL
cursor.execute('INSERT INTO `pedidos` (`idProducto`, `cantidad`, `precioTotal`, `idUsuario`) VALUES (?,?,?,?)',
               ( 101, 2, 200, 1),
( 102, 1, 150, 2),
( 103, 3, 300, 3),
( 101, 1, 100, 4),
( 102, 2, 300, 5),
( 104, 1, 50, 6),
( 105, 4, 600, 7),
( 103, 1, 100, 8),
( 106, 2, 300, 9),
( 101, 3, 300, 10),
( 102, 1, 150, 11),
( 103, 2, 200, 12),
( 104, 1, 50, 13),
( 105, 5, 750, 14),
( 106, 3, 450, 15),
( 101, 2, 200, 16),
( 102, 1, 150, 17),
( 103, 2, 200, 18),
( 104, 1, 50, 19),
( 105, 4, 600, 20))
#Paso 3.1. PARA CONSULTAS SELECT - RECUPERAR LOS DATOS
#usuarios=cursor.fetchall()
#Mostrar los datos
#for usuario in usuarios:
    #print(usuario[1],"Edad:",usuario[2],"años")


#Paso 4. Enviar los cambios a la Base de Datos
conexion.commit()
