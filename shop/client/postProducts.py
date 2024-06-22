import requests

response = requests.get('https://fakestoreapi.com/products')
products = response.json()

url = 'http://127.0.0.1:8000/api/products/'
category_url = 'http://127.0.0.1:8000/api/category/'

categories_response = requests.get(category_url)

categories = categories_response.json()
category_map = {category['name']: category['id'] for category in categories}

for product in products:

    category_name = product['category']
    category_id = category_map.get(category_name)

    data = {
        'name': product['title'],
        'description': product['description'],
        'price': product['price'],
        'category': category_id
    }
    response_post = requests.post(url, data=data)
    print(response_post.status_code, response_post.json())
