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
        <div>
            <h2>{restaurant.name}</h2>
            <p>Address: {restaurant.address}</p>
            <h3>Pizzas</h3>
            <ul>
                {restaurant.pizzas.map((pizza) => (
                    <li key={pizza.id}>
                        {pizza.name} - {pizza.ingredients}
                    </li>
                ))}
            </ul>
        </div>
    );
}