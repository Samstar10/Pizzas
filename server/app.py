import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response, request, jsonify, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(
    __name__,
    # static_url_path='',
    # static_folder='static',
    # template_folder='templates'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)



if __name__ == '__main__':
    app.run(port=5555)