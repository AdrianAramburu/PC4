def guardar_tabla_multiplicar():
    numero = int(input("Digite un número entero entre 1 y 10: "))

    
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"

    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            resultado = numero * i
            linea = f"{numero} x {i} = {resultado}\n"
            archivo.write(linea)

    print(f"La tabla de multiplicar del número {numero} ha sido guardada en el archivo {nombre_archivo}.")


def mostrar_tabla_multiplicar():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))

    
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"

    try:
        with open(nombre_archivo, "r") as archivo:
            tabla = archivo.read()

            if not tabla:
                print(f"No se encontró la tabla de multiplicar del número {numero}.")
            else:
                print(f"Tabla de multiplicar del número {numero}:")
                print(tabla)

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")


def mostrar_linea_tabla():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    linea = int(input("Ingrese el número de línea a mostrar (entre 1 y 10): "))

   
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"

    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                print(f"No se encontró la tabla de multiplicar del número {numero}.")
            elif linea > len(lineas):
                print(f"No existe la línea {linea} en la tabla de multiplicar del número {numero}.")
            else:
                print(f"Línea {linea} de la tabla de multiplicar del número {numero}:")
                print(lineas[linea - 1].strip())

    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")


def mostrar_menu():
    print("====================MENU DE OPCIONES====================")
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            guardar_tabla_multiplicar()
        elif opcion == "2":
            mostrar_tabla_multiplicar()
        elif opcion == "3":
            mostrar_linea_tabla()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
