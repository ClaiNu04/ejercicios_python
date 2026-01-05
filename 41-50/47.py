




while True:
    print("Selecciona una opcion:")
    print("1. suma")
    print("2. resta")
    print("3 salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("Suma") 
    elif opcion == 2:
        print("Resta")
    elif opcion == 3:
        break
    else:
        print("Opcion invalida")
