import React from 'react';
import './Home.css'; // Import the CSS file

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1 className="home-title">Welcome to stayComitted!</h1>
        <p className="home-description">
          Achieve your goals and build better habits with our platform. Get started by creating an account or exploring your goals and habits.
        </p>
        <a href="/users" className="home-button">Get Started</a>
      </header>
    </div>
  );
};

export default Home;
