import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function RestaurantDetails() {

    const [restaurant, setRestaurant] = useState(null);
    const { id } = useParams();

    useEffect(() => {
        fetch(`/restaurants/${id}`)
          .then((response) => response.json())
          .then((data) => setRestaurant(data))
          .catch((error) => console.error('Error fetching restaurant:', error));
      }, [id]);


    if (!restaurant) {
        return <div>Loading...</div>;
    }

    return (
        <div className="container">
            <h2 className="heading">{restaurant.name}</h2>
            <p>Address: {restaurant.address}</p>
            <h3 className="sub-heading">Pizzas</h3>
            <ul className="pizza-list">
                {restaurant.pizzas.map((pizza) => (
                    <li key={pizza.id} className="pizza-item">
                        {pizza.name} - {pizza.ingredients}
                    </li>
                ))}
            </ul>
        </div>
    );
}