import requests
import csv
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        precio = data['bpi']['USD']['rate']
        return precio
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", str(e))
        return None

def guardar_en_archivo_texto(precio):
    try:
        with open('bitcoin.txt', 'w') as archivo:
            archivo.write(precio)
        print("Datos guardados en el archivo bitcoin.txt")
    except IOError as e:
        print("Error al guardar los datos en el archivo:", str(e))

def guardar_en_archivo_csv(precio):
    try:
        with open('bitcoin.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Fecha', 'Precio'])
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), precio])
        print("Datos guardados en el archivo bitcoin.csv")
    except IOError as e:
        print("Error al guardar los datos en el archivo:", str(e))

#Bitcoin
precio_bitcoin = obtener_precio_bitcoin()

# Guardar en archivo texto
guardar_en_archivo_texto(precio_bitcoin)

# Guardar en archivo CSV
guardar_en_archivo_csv(precio_bitcoin)
