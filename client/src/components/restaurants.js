import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

export default function Restaurants() {

    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch('/restaurants')
          .then((response) => response.json())
          .then((data) => setRestaurants(data))
          .catch((error) => console.error('Error fetching restaurants:', error));
      }, []);
        

    return (
        <div className="container">
            <h1 className="heading">Restaurants</h1>
            <ul className="restaurant-list">
                {restaurants.map((restaurant) => (
                    <li key={restaurant.id} className="restaurant-item">
                        <NavLink to={`/restaurants/${restaurant.id}`}>{restaurant.name}</NavLink>
                    </li>
                ))}
            </ul>
        </div>
    );
}