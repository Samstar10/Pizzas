import React from 'react';
import './App.css';
import Restaurants from './components/restaurants';
import RestaurantDetails from './components/restaurantDetails';
import Pizzas from './components/pizzas';

function App() {
  return (
    <div>
      <Restaurants />
      <RestaurantDetails />
      <Pizzas />
    </div>
  );
}

export default App;
