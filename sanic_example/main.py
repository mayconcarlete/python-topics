import asyncio
from sanic import Sanic
from routes import load_routes
from async_fetch_controller import load_multiple_requests, make_request
from sanic.response import json

app = Sanic('my_sanic_app')

# load_routes(app)
# load_multiple_requests(app)
@app.get('/multiple')
async def get_all(request):
    body = make_request()
    return json(body)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(app.run(host='0.0.0.0', port=3000, auto_reload=True))
    app.run(host='0.0.0.0', port=3000, auto_reload=True)
