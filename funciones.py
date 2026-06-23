# FUNCIONES 

def menu():
	print(f"1. Agrega Una Tarea a la Lista")
	print(f"2. Muestre Las tareas")
	print(f"3. Marque una tarea completada")
	print(f"4. Eliminar una tarea de la lista")
	print(f"5. Salir")
	eleccion = input(f"Elija una opcion: ")
	return eleccion
	
def procesar(eleccion,lista):
	
	if eleccion == "1":
		agregar = input("Escriba la tarea que quiere agregar: ")
		lista.append(agregar)
		
	elif eleccion == "2":
			
		if len(lista) == 0:
			print("\nNo hay tareas pendientes. 🎉\n")
				
		else:
			print("\n--- TAREAS ---")
					
			for indice, tareas in enumerate(lista):
				print(f"{indice + 1}. {tareas}")
			
	elif eleccion == "3":
		completo = int(input("Ingrese el numero de la tarea completada: "))
		if 1 <= completo <= len(lista):
			lista[completo - 1] += " (COMPLETADO)"
			print("¡Tarea marcada como completada!")
		else:
			print("Número de tarea no válido.")
	
	elif eleccion == 4:
		eliminar = int(input("Ingrese el numero de la tarea a eliminar: "))
		if 1 <= eliminar <= len(lista):
			
			print(f"Va a eliminar: {lista[eliminar - 1]}")
			
			lista.pop(eliminar - 1)
			
			print("¡Tarea eliminada!")
		else:
			print("Número de tarea no válido.")
