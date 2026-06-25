# FUNCIONES 

def menu():
	print()
	print(" ---- MENU ----")
	print()
	print(f"1. Agrega Una Tarea a la Lista")
	print()
	print(f"2. Marque una tarea completada")
	print()
	print(f"3. Eliminar una tarea de la lista")
	print()
	print(f"4. Salir")
	print()
	eleccion = input(f"Elija una opcion: ")
	return eleccion
	
def procesar(eleccion,lista):
	
	if eleccion == "1":
		agregar = input("Escriba las tareas que quiere agregar(para salir ingrese FIN): ")
		
		while agregar != "FIN":
			lista.append(agregar)
			
			
			agregar = input("Escriba las tareas que quiere agregar(para salir ingrese FIN): ")
			
		
	elif eleccion == "2":
		
		completo = int(input("Ingrese el numero de la tarea completada: "))
		if 1 <= completo <= len(lista):
			lista[completo -1] += " (!!COMPLETADO!!)"
			print("¡Tarea marcada como completada!")
		else:
			print("Número de tarea no válido.")
	
	elif eleccion == "3":
		eliminar = int(input("Ingrese el numero de la tarea a eliminar: "))
		if 1 <= eliminar <= len(lista):
			
			print(f"Va a eliminar: {lista[eliminar-1]}")
			
			lista.pop(eliminar)
			
			print("¡Tarea eliminada!")
	else:
		print("Número de tarea no válido.")
