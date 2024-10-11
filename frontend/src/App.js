import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home/Home';
import Blockchain from './components/Blockchain/Blockchain';
import ConductTransaction from './components/Conduct_Transaction/Conduct_Transaction';
import BNav from './components/BNav/BNav'
import TransactionPool from './components/TransactionPool/TransactionPool';

const App = () => {
  return (
    <Router>
      <BNav/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/blockchain" element={<Blockchain />} />
        <Route path="/conduct-transaction" element={<ConductTransaction />} />
        <Route path="/transaction-pool" element={<TransactionPool/>} />
      </Routes>
    </Router>
  );
};

export default App;
