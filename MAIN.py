# MAIN PROGRAMA

from funciones import *

tareas = []
eleccion = ""

while eleccion != "5":
	eleccion = menu()
	
	if eleccion != "5":
		procesar(eleccion,tareas)
		
print("Adios!")
