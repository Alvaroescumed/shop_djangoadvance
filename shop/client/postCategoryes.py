import requests

# Obtener los datos de la API externa
response = requests.get('https://fakestoreapi.com/products/categories')
categories = response.json()

url = 'http://127.0.0.1:8000/api/category/'


for category in categories:
    data = {
        'name': category,
    }
    response_post = requests.post(url, data=data)
    print(response_post.status_code, response_post.json())
