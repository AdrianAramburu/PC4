import requests

url = " https://images.unsplash.com/photo-1575383095193-52195a64e3a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHBlcnJpdG98ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60" 
respuesta = requests.get(url)

with open('perrito_bonito.jpg', 'wb') as f:
    f.write(respuesta.content)
    pass