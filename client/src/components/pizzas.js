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
        <div className="container">
            <h2 className="heading">Pizzas</h2>
            <ul className="pizza-list">
                {pizzas.map((pizza) => (
                    <li key={pizza.id} className="pizza-item">
                        {pizza.name} - {pizza.ingredients}
                    </li>
                ))}
            </ul>
        </div>
    );
}