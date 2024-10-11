import React from 'react';
import { Link } from 'react-router-dom';
import './BNav.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="nav-links">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/blockchain">Blockchain</Link>
        </li>
        <li>
          <Link to="/conduct-transaction">Conduct Transaction</Link>
        </li>
        <li>
          <Link to="/transaction-pool">Transaction Pool</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
