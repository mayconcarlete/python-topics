from sanic import Sanic
from sanic.response import json
from request import multiple_requests

async def make_request(request):
    urls = [
        'https://fakerapi.it/api/v1/addresses?_quantity=1',
        'https://api.pokemontcg.io/v2/cards?q=name:gardevoir'
    ]
    response = await multiple_requests(urls)
    return json(response, status=200)



async def load_multiple_requests(app: Sanic):
    app.add_route(make_request, '/multiple', methods=['GET'])
