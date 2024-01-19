import React from "react";
import { NavLink } from "react-router-dom";

export default function Home() {

    return (
        <div>
            <NavLink to="/restaurants">Restaurants</NavLink>
            <NavLink to="/pizzas">Pizzas</NavLink>
        </div>
    );
}