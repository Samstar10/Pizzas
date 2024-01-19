import React, { useEffect, useState } from "react";

export default function Restaurants() {

    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch('/restaurants')
          .then((response) => response.json())
          .then((data) => setRestaurants(data))
          .catch((error) => console.error('Error fetching restaurants:', error));
      }, []);
        

    return (
        <div>
            <h1>Restaurants</h1>
            <ul>
                {restaurants.map((restaurant) => (
                    <li key={restaurant.id}>
                        {restaurant.name}, {restaurant.address}
                    </li>
                ))}
            </ul>
        </div>
    );
}