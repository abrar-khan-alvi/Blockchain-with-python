import React from 'react';
import './Home.css';
import logo from '../../assets/Picture1.png';
import WalletInfo from '../WalletInfo/WalletInfo';
import { API_BASE_URL } from '../../config';
import { Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const fetchMineBlock = () => {
    fetch(`${API_BASE_URL}/blockchain/mine`)
      .then(() => {
        alert('Success!');

        navigate('/blockchain');
      });
  }
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Welcome to BongoChain</h1>
      </header>
      <div className="logo-container">
        <img src={logo} alt="BongoCoin Logo" className="bongocoin-logo" />
      </div>
      <WalletInfo/>
      <hr />
      <Button
        variant="danger"
        onClick={fetchMineBlock}
      >
        Mine a block of these transactions
      </Button>
    </div>
  );
};

export default Home;
