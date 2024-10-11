import React, { useState, useEffect } from 'react';
import { API_BASE_URL } from '../../config.js';

const WalletInfo = () => {
    const [walletInfo, setWalletInfo] = useState(null);
    const [loading, setLoading] = useState(true); 
    const [error, setError] = useState(null); 

    useEffect(() => {
        setLoading(true);
        setError(null);

        fetch(`${API_BASE_URL}/wallet/info`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((json) => {
                setWalletInfo(json); 
            })
            .catch((err) => {
                setError(err.message); 
            })
            .finally(() => {
                setLoading(false); 
            });
    }, []);

    if (loading) {
        return <div className="loading-message">Loading wallet info...</div>; 
    }

    if (error) {
        return <div className="error-message">Error: {error}</div>; 
    }

    return (
        <div className="wallet-info-container">
            <h3>Wallet Information</h3>
            {walletInfo && (
                <div>
                    <p><strong>Address:</strong> {walletInfo.address}</p>
                    <p><strong>Balance:</strong> {walletInfo.balance}</p>
                </div>
            )}
        </div>
    );
};

export default WalletInfo;
