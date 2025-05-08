<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to the Ultimate Cloud Project."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to the Ultimate Cloud Project."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> adddd9c236f0de6cd5aa034f8a9a1d43aed864fb
