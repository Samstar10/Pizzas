import React , { useEffect, useState } from "react";

export default function Pizzas() {

    const [pizzas, setPizzas] = useState([]);

    useEffect(() => {
        fetch('/pizzas')
          .then((response) => response.json())
          .then((data) => setPizzas(data))
          .catch((error) => console.error('Error fetching pizzas:', error));
      }, []);

    return (
        <div>
            <h2>Pizzas</h2>
            <ul>
                {pizzas.map((pizza) => (
                    <li key={pizza.id}>
                        {pizza.name} - {pizza.ingredients}
                    </li>
                ))}
            </ul>
        </div>
    );
}