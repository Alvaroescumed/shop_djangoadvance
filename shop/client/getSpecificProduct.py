import requests
from getpass import getpass
from pprint import pprint 
# Obtener los datos de la API externa

url = 'http://127.0.0.1:8000/api/products/2'
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
        "Authorization": f'Token {token}'
    }

    res = requests.get(url, headers=headers)

    pprint(res.json())
