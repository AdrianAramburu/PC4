import requests

def precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()  
        data = respuesta.json()
        precio = data['bpi']['USD']['rate_float']
        return precio
    except (requests.RequestException, KeyError):
        print('Hubo un error al obtener el precio actual del Bitcoin...')
        return None

def costo_bitcoins(n):
    precio = precio_bitcoin()
    if precio is not None:
        costo = n * precio
        print(f'El costo actual de {n:,.4f} Bitcoins en USD es: ${costo:,.4f}')  #Esto se va ir actualizando segun la pagina


while True:
    try:
        cantidad_bitcoins = float(input('Digite la cantidad de Bitcoins que posee: '))
        break
    except ValueError:
        print('Hubo un error, digite un numero valido porfavor.')

costo_bitcoins(cantidad_bitcoins)

