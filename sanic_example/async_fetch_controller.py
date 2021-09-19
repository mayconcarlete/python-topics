from sanic import Sanic
from sanic.response import json
from request import multiple_requests

def make_request():
    urls = [
        'https://fakerapi.it/api/v1/addresses?_quantity=1',
        'https://api.pokemontcg.io/v2/cards?q=name:gardevoir'
    ]
    response = multiple_requests(urls)
    return response



def load_multiple_requests(app: Sanic):
    app.add_route(make_request, '/multiple', methods=['GET'])
