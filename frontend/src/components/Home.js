// src/components/Home.js
import React from 'react';
import './Home.css';
import logo from '../assests/Picture1.png';  // Adjust path if necessary

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Welcome to BongoChain</h1>
        <p>The future of decentralized finance in Bangladesh.</p>
        <button className="learn-more-btn">Learn More</button>
      </header>
      
      <div className="logo-container">
        <img src={logo} alt="BongoCoin Logo" className="bongocoin-logo" />
      </div>

      <section className="about-section">
        <h2>About BongoChain</h2>
        <p>
          BongoCoin is a revolutionary blockchain solution built to empower financial transactions
          with efficiency and security, designed for the people of Bangladesh.
        </p>
      </section>
    </div>
  );
};

export default Home;
