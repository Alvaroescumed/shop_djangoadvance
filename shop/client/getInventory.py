import requests
from getpass import getpass
from pprint import pprint  
# usamos pprint para que la respuesta en el terminal esté en formato json y no como un bloque de terxto

url = 'http://127.0.0.1:8000/api/inventory/'
endpoint = 'http://127.0.0.1:8000/auth/'

username = input('Usuario:')
password = getpass('Contraseña:')
token_res = requests.post(endpoint, json={
    'username':username, 
    'password':password
    })

if token_res.status_code == 200:
    token = token_res.json()['token']
    headers= {
        "Authorization": f'Token {token}',
    }

    res = requests.get(url, headers=headers)

    pprint(res.json())

else:
    print("Error al obtener el token")