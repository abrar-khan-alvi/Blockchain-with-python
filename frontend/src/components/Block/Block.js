import React, { useState } from 'react';
import { MILLISECONDS_PY } from '../../config';
import './Block.css';
import Transaction from '../Transaction/Transaction';
import { Modal, Button } from 'react-bootstrap';

function TransactionModal({ block, show, handleClose }) {
  const { data } = block;

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Transaction Details</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {data.length > 0 ? (
          data.map((transaction) => (
            <div key={transaction.id} className="Transaction">
              <hr />
              <Transaction transaction={transaction} />
            </div>
          ))
        ) : (
          <p>No transactions available</p>
        )}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

function Block({ block }) {
  const { timestamp, hash } = block;
  const hashDisplay = `${hash.substring(0, 15)}...`;
  const timestampDisplay = new Date(timestamp / MILLISECONDS_PY).toLocaleString();
  
  const [showModal, setShowModal] = useState(false);

  const handleShow = () => setShowModal(true);
  const handleClose = () => setShowModal(false);

  return (
    <div className="Block">
      <div className="hash">Hash: {hashDisplay}</div>
      <div className="timestamp">Timestamp: {timestampDisplay}</div>

      <Button variant="primary" onClick={handleShow} className="toggle-btn">
        Show Transactions
      </Button>

      {/* Modal for displaying transactions */}
      <TransactionModal block={block} show={showModal} handleClose={handleClose} />
    </div>
  );
}

export default Block;
