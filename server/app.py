import os

# from dotenv import load_dotenv
# load_dotenv()

from flask import Flask, make_response, request, jsonify, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(
    __name__,
    # static_url_path='',
    # static_folder='static',
    # template_folder='templates'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Restaurants(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_dict = [
            {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            } for restaurant in restaurants
        ]

        return make_response(jsonify(restaurants_dict), 200)





api.add_resource(Restaurants, '/restaurants')

if __name__ == '__main__':
    app.run(port=5555)