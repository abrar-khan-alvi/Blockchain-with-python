import React from 'react';
import './Transaction.css'
const Transaction = ({transaction}) => {
    const {input, output} = transaction;
    const recipients = Object.keys(output);

    return (
        <div className=' text-center'>  
            <div className="Transaction">From:: { input.address }</div>
            {
                recipients.map(recipient =>(
                    <div key={recipient}> 
                        To: {recipient} | Sent:{output[recipient]}
                    </div>
                ))
            }
            
        </div>
    );
};

export default Transaction;