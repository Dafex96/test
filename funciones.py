usuarios = {}

def menu():
    print("MENÚ PRINCIPAL")
    print("1) Ingresar usuario: ")
    print("2) Buscar usuario: ")
    print("3) Eliminar usuario: ")
    print("4) Salir: ")

def agregar():
    
    nombre = input("Ingrese el nombre se usuario: ").lower()
    sexo = input("Ingrese el sexo (M:Masculino), (F:Femenino): ").upper()
    
    while True:
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Debe ingresar solamente 'M' para masculino y 'F' para Femenino")
            sexo = input("Ingrese el sexo (M:Masculino), (F:Femenino): ").upper()
    
    contra = input("Ingrese la contraseña: ").lower()
    if len(contra) < 8:
        print("La contraseña debe tener minimo 8 caracteres")
        contra = input("Ingrese la contraseña: ")
    if "1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or"0" not in contra:
        print("La contraseña debe tener al menos un numero")
        contra = input("Ingrese la contraseña: ")
    
    letra = False
    
    for l in contra:
        if 'a' <= l.lower() <= 'z':
            letra = True
        if not letra:
            print("La contraseña debe tener al menos una  letra")
        contra = input("Ingrese la contraseña: ")
        if ' ' in contra:
            print("La contraseña no debe tener espacios")
            contra = input("Ingrese la contraseña: ")
        usuarios[nombre] = {"nombre": nombre,"sexo": sexo,"contraseña":contra}
        print("¡Usuario añadido!")
        return False

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
