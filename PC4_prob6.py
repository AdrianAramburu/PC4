import sqlite3
import requests
from datetime import datetime

def tener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        precios = data['bpi']
        return precios
    except requests.RequestException as e:
        print("Error al obtener los precios de Bitcoin:", str(e))
        return None

def generar_tablabitcoin():
    try:
        conexion = sqlite3.connect('cryptos.db')
        cursor = conexion.cursor()

        # Crear la tabla bitcoin si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           fecha TEXT,
                           usd REAL,
                           gbp REAL,
                           eur REAL)''')

        conexion.commit()
        print("Tabla bitcoin creada exitosamente.")
    except sqlite3.Error as e:
        print("Error al crear la tabla bitcoin:", str(e))
    finally:
        if conexion:
            conexion.close()

def insertar_precio_bitcoin():
    try:
        precios = tener_precio_bitcoin()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        conexion = sqlite3.connect('cryptos.db')
        cursor = conexion.cursor()

        # Insertar los precios en la tabla bitcoin
        cursor.execute('''INSERT INTO bitcoin (fecha, usd, gbp, eur)
                          VALUES (?, ?, ?, ?)''', (fecha, precios['USD']['rate'], precios['GBP']['rate'], precios['EUR']['rate']))

        conexion.commit()
        print("Datos insertados exitosamente en la tabla bitcoin.")
    except sqlite3.Error as e:
        print("Error al insertar los datos en la tabla bitcoin:", str(e))
    finally:
        if conexion:
            conexion.close()


generar_tablabitcoin()
insertar_precio_bitcoin()
