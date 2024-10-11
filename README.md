
**activate the virtual environment in vs code**
```
python -m venv .env

.env\Scripts\activate

```
here .env is folder name

**install all packages**
```
pip install pytest
pip install -r requirements.txt
python -m pip install flask
```
**Run the tests**
Make sure to activate the virtual environment.
```
python -m pytest backend/tests
```

```
python -m backend.blockchain.block 
```

**Run the application and API**
Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**
Make sure to activate the virtual environment.

```
set PEER=True
python -m backend.app
```

**Run the frontend**

In the frontend directory:

```
npm run start
```

**Seed the backend with data**
Make sure to activate the virtual environment.

```
set SEED_DATA=True
python -m backend.app
```
***

![Frontend](images/Screenshot%202024-10-11%20182722.png)

**How the Application Works:**

1. Create a Wallet: Generate a new wallet with a public/private key pair.
2. Submit Transactions: Using the wallet’s private key, submit transactions (e.g., send cryptocurrency to another wallet).
3. Mine New Blocks: Mine a new block that validates pending transactions from the pool and appends them to the blockchain.
4. Explore the Blockchain: View all blocks and their transaction history using the blockchain explorer.