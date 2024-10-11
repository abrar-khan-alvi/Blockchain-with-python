import React, { useState, useEffect } from 'react';

const Joke = () => {
    const [joke, setJoke] = useState(null); // State to store the joke

    useEffect(() => {
        fetch('https://official-joke-api.appspot.com/jokes/random')
        .then(response=>response.json())
        .then(json=>setJoke(json))
    }, []);

    return (
        <div>
            <h3>Random Joke</h3>
            {joke && (
                <div>
                    <p><strong>Setup:</strong> {joke.setup}</p>
                    <p><strong>Punchline:</strong> {joke.punchline}</p>
                </div>
            )}
        </div>
    );
};

export default Joke;
