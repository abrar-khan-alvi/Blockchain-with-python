**activate the virtual environment in vs code**
```
python -m venv .env

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