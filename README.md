# Pizzas API

## Author: Samuel Muli

This API provides endpoints to manage and retrieve information about restaurants. With this API, developers can easily integrate restaurant-related functionality into their applications. The API supports JSON format for data exchange and it follows RESTful principles for a clear and intuitive interface.

In this repo, is a Flask application with some features built out. There
is also a fully built React frontend application, so you can test if the API is
working.

## Setup

To download the dependencies for the frontend and backend, run:

```sh
pipenv install
npm install --prefix client
```

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by running:

```sh
python app.py
```

You can run your React app on [`localhost:4000`](http://localhost:4000) by running:

```sh
npm start --prefix client
```

## Models

These are the relationships:

- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`

```
+-------------+       +----------------+       +-------------+
| Restaurant  |       | RestaurantPizza|       | Pizza       |
+-------------+       +----------------+       +----------+
| id          |       | id             |       | id          |
| name        |       | restaurant_id  |       | name        |
| address     |       | pizza_id       |       | ingredients |
+-------------+       | price          |       +-------------+
                      +----------------+

```

Then, run the migrations and seed file:

```sh
flask db upgrade
python app/seed.py
```

> If you aren't able to get the provided seed file working, you are welcome to
> generate your own seed data to test the application.

## Routes

### GET /restaurants:

Returns JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]
```

### GET /restaurants/:id

If the `Restaurant` exists, returns JSON data in the format below:

```json
{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```

If the `Restaurant` does not exist, returns the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas

Returns JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

### POST /restaurant_pizzas

This route creates a new `RestaurantPizza` that is associated with an
existing `Pizza` and `Restaurant`. It accepts an object with the following
properties in the body of the request:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

If the `RestaurantPizza` is created successfully, sends back a response with the data
related to the `Pizza`:

```json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```

If the `RestaurantPizza` is **not** created successfully, returns the following
JSON data, along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```


## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Add feature/fix bug"`
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

Please ensure that your code follows the project's coding style and includes appropriate tests.

## License

The Project Name is open source and is released under the [MIT License](LICENSE).