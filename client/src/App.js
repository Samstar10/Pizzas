import React from 'react';
import './App.css';
import Restaurants from './components/restaurants';
import RestaurantDetails from './components/restaurantDetails';
import Pizzas from './components/pizzas';
import AddPizzaFormComponent from './components/AddPizzaFormComponent';

function App() {
  return (
    <div>
      <Restaurants />
      <RestaurantDetails />
      <Pizzas />
      <AddPizzaFormComponent />
    </div>
  );
}

export default App;
