import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import Restaurants from './components/restaurants';
import RestaurantDetails from './components/restaurantDetails';
import Pizzas from './components/pizzas';
import AddPizzaFormComponent from './components/AddPizzaFormComponent';
import Home from './components/home';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/restaurants" element={<Restaurants />} />
        <Route path="/restaurants/:id" element={<RestaurantDetails />} />
        <Route path="/pizzas" element={<Pizzas />} />
        <Route path="/restaurant_pizzas" element={<AddPizzaFormComponent />} />
      </Routes>
    </div>
  );
}

export default App;
