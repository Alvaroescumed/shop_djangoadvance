import requests
from getpass import getpass
from pprint import pprint 

url = 'http://127.0.0.1:8000/viewset/products/by_category/'

category= input('ID Categoria:')
params= {
    'category_id': category
}

res = requests.get(url, params= params)

pprint(res.json())
