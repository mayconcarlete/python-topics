from sanic import Sanic
from routes import load_routes


app = Sanic('my_sanic_app')

load_routes(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, auto_reload=True)
