from pyfiglet import Figlet
import random

# Crear una instancia de Figlet
figlet = Figlet()

# LISTA DE FUENTES 
fuentes_disponibles = figlet.getFonts()

# MUESTRO LA LISTA DE FUENTES DISPONIBLES PARA QUE EL USUARIO PUEDA ESCRIBARLA
print("Fuentes disponibles: " + ", ".join(fuentes_disponibles))

fuente_usuario = input("Ingrese el nombre de la fuente (deje vacío para seleccionar aleatoriamente): ")

# FUENTE DE FORMA ALEATORIA CUANDO SE DEJA VACIO
if not fuente_usuario:
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Se ha seleccionado la fuente aleatoriamente: {fuente_seleccionada}")
else:
    
    if fuente_usuario in fuentes_disponibles:
        fuente_seleccionada = fuente_usuario
    else:
        print("Fuente no válida. Se utilizará la fuente por defecto.")
        fuente_seleccionada = figlet.DEFAULT_FONT


figlet.setFont(font=fuente_seleccionada)


texto_usuario = input("Ingrese el texto a imprimir: ")

# EL TEXTO GENERADO
texto_generado = figlet.renderText(texto_usuario)
print(texto_generado)
