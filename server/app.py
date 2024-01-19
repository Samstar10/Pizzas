import os

from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response, request, jsonify, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template('index.html')

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
    
class RestaurantsById(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:
            restaurant_dict = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': []
            }

            for restaurant_pizza in restaurant.restaurant_pizzas:
                pizza = Pizza.query.filter_by(id=restaurant_pizza.pizza_id).first()

                pizza_dict = {
                    'id': pizza.id,
                    'name': pizza.name,
                    'ingredients': pizza.ingredients
                }

                restaurant_dict['pizzas'].append(pizza_dict)

            return make_response(jsonify(restaurant_dict), 200)
        
        else:
            return make_response(jsonify({'error': 'Restaurant not found'}), 404)
        

    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return make_response(jsonify({'message': 'Restaurant deleted'}), 200)
        
        else:
            return make_response(jsonify({'error': 'Restaurant not found'}), 404)
        

class Pizzas(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_dict = [
            {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            } for pizza in pizzas
        ]

        return make_response(jsonify(pizzas_dict), 200)
    

class RestaurantPizzas(Resource):
    def post(self):
    
        data = request.get_json()

        price = int(data['price'])
        pizza_id = int(data['pizza_id'])
        restaurant_id = int(data['restaurant_id'])

        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

        try:
            db.session.add(restaurant_pizza)
            db.session.commit()

            pizza = Pizza.query.filter_by(id=pizza_id).first()

            pizza_dict = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }

            return make_response(jsonify(pizza_dict), 201)

        except:
            return make_response(jsonify({'error': 'Something went wrong'}), 500)



api.add_resource(Restaurants, '/restaurants')
api.add_resource(RestaurantsById, '/restaurants/<int:id>')
api.add_resource(Pizzas, '/pizzas')
api.add_resource(RestaurantPizzas, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555)