from flask import Flask

app = Flask(__name__)

@app.route('/')

def default():
    return f'<h1>Welcome to the blockchain</h1>'
def test():
    return 'Test'

app.run()