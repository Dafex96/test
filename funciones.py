usuarios = {}

def menu():
    print("MENÚ PRINCIPAL")
    print("1) Ingresar usuario: ")
    print("2) Buscar usuario: ")
    print("3) Eliminar usuario: ")
    print("4) Salir: ")

def agregar():
    
    nombre = input("Ingrese el nombe se usuario: ").lower()
    sexo = input("Ingrese el sexo (M:Masculino), (F:Femenino): ").upper()
    
    while sexo == "M" and sexo == "F":
        break
    else:
        print("Debe ingresar 'M' para Masculino y 'F' para Femenino.")
        sexo = input("Ingrese el sexo: ").upper()
    
    contra = input("Ingrese la contraseña: ")

    usuarios[nombre] = {"nombre": nombre,"sexo": sexo,"contraseña":contra}
    print("¡Usuario añadido!")

def buscar():
    nombre = input("Inserte el nombre de usuario a buscar: ").lower()
    for n in usuarios.values():
        if n["nombre"] == nombre:
            print(f"Sexo: {n['sexo']}, Contraseña: {n['contraseña']}")
            return
    print("Usuario ingresado no existe.")

def eliminar():
    nombre = input("Ingrese el usuario a eliminar: ")
    for nombre, n in list(usuarios.items()):
        if n["nombre"] == nombre:
            del usuarios[nombre]
            print("¡Usuario eliminado!")
            return
    print("Usuario no encontrado.")
