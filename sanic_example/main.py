import asyncio
from sanic import Sanic
# from routes import load_routes
from async_fetch_controller import load_multiple_requests, make_request
from sanic.response import json

app = Sanic('my_sanic_app')

# load_routes(app)
# load_multiple_requests(app)

# @app.get('/multiple')
# async def get_all(request):
#     body = await make_request()
#     return json(body)


loop = asyncio.get_event_loop()
loop.run_until_complete(load_multiple_requests(app))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, auto_reload=True)
