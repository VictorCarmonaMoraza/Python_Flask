
#Creamos un fichero, w es modo escritura
fichero = open("Datos.txt","w")
fichero.write("Estos son los datos para el fichero")
fichero.close()

# modo lectura, da error sin try 
try:
    fichero = open("Datos3.txt","r")
    fichero.write("Estos son los datos para el fichero")
    fichero.close()
except IOError:
    print("El fichero no existe")
except:
    print("Error General")
else:
    print("Tratamiento del fichero correcto")
finally:
    print("Tratamiento del fichero finalizado")

print("Continua el programa")