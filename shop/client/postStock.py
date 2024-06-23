import requests
from getpass import getpass
from pprint import pprint 


url = 'http://127.0.0.1:8000/api/inventory/'
endpoint = 'http://127.0.0.1:8000/auth/'

username = input('Usuario:')
password = getpass('Contraseña:')
token_res = requests.post(endpoint, json={
    'username':username, 
    'password':password
    })

data = {
#     "product": 1,
#     "quantity": 50
#    }
# #   {
# #     "product": 2,
# #     "quantity": 100
# #   },
# #   {
# #     "product": 5,
# #     "quantity": 20
# #   },
# #   {
    "product": 9,
    "quantity": 30
  }


if token_res.status_code == 200:
    token = token_res.json()['token']
    headers= {
        "Authorization": f'Token {token}',
    }

    res = requests.post(url, headers=headers, data=data)

    pprint(res.json())

else:
    print("Error al obtener el token")
