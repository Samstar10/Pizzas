from faker import Faker
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

def seed_data():
    # Create Restaurants
    for _ in range(5):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        db.session.add(restaurant)

    db.session.commit()

    # Create Pizzas
    for _ in range(10):
        pizza = Pizza(
            name=fake.word(),
            ingredients=", ".join(fake.words(5))
        )
        db.session.add(pizza)

    db.session.commit()

    # Create RestaurantPizzas
    for _ in range(20):
        restaurant_id = fake.random_element(elements=[r.id for r in Restaurant.query.all()])
        pizza_id = fake.random_element(elements=[p.id for p in Pizza.query.all()])
        price = fake.random_int(min=1, max=30)

        restaurant_pizza = RestaurantPizza(
            restaurant_id=restaurant_id,
            pizza_id=pizza_id,
            price=price
        )
        db.session.add(restaurant_pizza)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
