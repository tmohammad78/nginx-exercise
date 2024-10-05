from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return f"Response from Server 1 - ID: {random.randint(1, 100)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
