import React from "react";
import { NavLink } from "react-router-dom";

export default function Home() {

    return (
        <div className="home-buttons">
            <NavLink to="/restaurants"><button>Restaurants</button></NavLink>
            <NavLink to="/pizzas"><button>Pizzas</button></NavLink>
        </div>
    );
}