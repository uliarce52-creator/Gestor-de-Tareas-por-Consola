# MAIN PROGRAMA

from funciones import *

tareas = []
eleccion = ""

while eleccion != "4":
	
	if len(tareas) == 0:
		print()
		print(f"La lista esta vacia")
		print()
	else:
		print()
		print(f"Su lista de tareas es la siguiente")
		print()
		for i,p in enumerate(tareas):
			print(f"{i} : {p}")
		print()
		print()
		
		
	eleccion = menu()
	
	if eleccion != "4":
		procesar(eleccion,tareas)
		
print("Adios!")

