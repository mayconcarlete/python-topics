from flask import Flask
from authlib.integrations.flask_client import OAuth
from flask.helpers import url_for
from flask import jsonify

app = Flask(__name__)

oauth = OAuth(app)

github = oauth.register('github')

@app.route('/login')
def login():
    redirect_url = url_for('authorize', _external=True)
    return github.authorize_redirect(redirect_url)

@app.route('/authorize')
def authorize():
    token = github.authorize_access_token()
    # you can save the token into database
    profile = github.get('/user', token=token)
    return jsonify(profile)        


if __name__ == '__main__':
    app.run()