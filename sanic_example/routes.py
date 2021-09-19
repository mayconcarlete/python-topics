from sanic.app import Sanic
from sanic.response import json


# http://0.0.0.0:3000/status?key=maycon
def status(request):
    return json({'message': f'ok {request.args}'}, status=200)


# http://0.0.0.0:3000/status/maykerops
def status_parameter(request, arg1):
    return json({'message': f'ok with arg: {arg1}'})

def post_status(request):
    return json({'message_post_body': request.json})


def load_routes(app: Sanic):
    app.add_route(status, '/status', methods = ['GET'])
    app.add_route(status_parameter, '/status/<arg1>', methods=['GET'])
    app.add_route(post_status, '/post', methods=['POST'])
