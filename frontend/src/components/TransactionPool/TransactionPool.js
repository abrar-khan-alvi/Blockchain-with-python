import React, { useState, useEffect } from 'react';
import Transaction from '../Transaction/Transaction';
import { API_BASE_URL, SECONDS_JS } from '../../config';

const POLL_INTERVAL = 10 * SECONDS_JS;

function TransactionPool() {
  const [transactions, setTransactions] = useState([]);

  // Fetch Transactions from API
  const fetchTransactions = () => {
    fetch(`${API_BASE_URL}/transactions`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`API call failed with status: ${response.status}`);
        }
        return response.json();
      })
      .then(json => {
        console.log('Fetched transactions:', json);
        setTransactions(json);
      })
      .catch(error => {
        console.error('Error fetching transactions:', error);
      });
  };

  // Use Effect to Poll the API
  useEffect(() => {
    fetchTransactions();

    // Poll transactions at a regular interval
    const intervalId = setInterval(fetchTransactions, POLL_INTERVAL);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="TransactionPool text-center">
      <hr />
      <h3>Transaction Pool</h3>

      {transactions.length > 0 ? (
        <div>
          {transactions.map(transaction => (
            <div key={transaction.id}>
              <hr />
              <Transaction transaction={transaction} />
            </div>
          ))}
        </div>
      ) : (
        <p>No transactions available in the pool</p>
      )}
    </div>
  );
}

export default TransactionPool;
