import React, { useEffect, useState } from "react";
import {  useNavigate } from "react-router-dom";

export default function AddPizzaFormComponent() {

    const [formData, setFormData] = useState({
        price: '',
        pizza_id: '',
        restaurant_id: '',
    });
    const [pizzas, setPizzas] = useState([]);
    const [restaurants, setRestaurants] = useState([]);

    const navigate = useNavigate();

    useEffect(() => {
        fetch('/pizzas')
          .then((response) => response.json())
          .then((data) => setPizzas(data))
          .catch((error) => console.error('Error fetching pizzas:', error));

        fetch('/restaurants')
          .then((response) => response.json())
          .then((data) => setRestaurants(data))
          .catch((error) => console.error('Error fetching restaurants:', error));

    }, []);


    function handleSubmit(event) {
        event.preventDefault();
        fetch('/restaurant_pizzas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Success:', data)
                setFormData({
                    price: '',
                    pizza_id: '',
                    restaurant_id: '',
                })
                navigate('/')
            })
            .catch((error) => console.error('Error:', error));
    }

    return (
        <form onSubmit={handleSubmit} className="add-pizza-form">
            <div className="price-field">
                <label className="label">
                    Price:
                    <input
                        type="text"
                        name="price"
                        value={formData.price}
                        onChange={(event) =>
                            setFormData({ ...formData, price: event.target.value })
                        }
                        className="input"
                    />
                </label>
            </div>
            <div className="pizza-field">
                <label className="label">
                    Pizza:
                    <select
                        name="pizza_id"
                        value={formData.pizza_id}
                        onChange={(event) =>
                            setFormData({ ...formData, pizza_id: event.target.value })
                        }
                        className="select"
                    >
                        {pizzas.map((pizza) => (
                            <option key={pizza.id} value={pizza.id}>
                                {pizza.name}
                            </option>
                        ))}
                    </select>
                </label>
            </div>
            <div className="restaurant-field">
                <label className="label">
                    Restaurant:
                    <select
                        name="restaurant_id"
                        value={formData.restaurant_id}
                        onChange={(event) =>
                            setFormData({ ...formData, restaurant_id: event.target.value })
                        }
                        className="select"
                    >
                        {restaurants.map((restaurant) => (
                            <option key={restaurant.id} value={restaurant.id}>
                                {restaurant.name}
                            </option>
                        ))}
                    </select>
                </label>
            </div>
            <button className="button" type="submit">Submit</button>
        </form>
    );
}