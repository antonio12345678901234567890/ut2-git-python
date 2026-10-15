print("1. Saludar\n2. Despedirse\n3. Salir")
opcion = input('Elija una opción: ')

match opcion:
    case "1":
        print("¡Hola!")
    case "2":
        print("¡Adios!")
    case "3":
        print("Saliendo...")
    case _:
        print("Opción no válida")
