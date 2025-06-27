from funciones import menu, agregar, buscar, eliminar

while True:
    try:
        menu()
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            agregar()
        elif opc == 2:
            buscar()
        elif opc == 3:
            eliminar()
        elif opc == 4:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, intente nuevamente.")
    except ValueError:
        print("Opcion invalida, intente nuevamente.")