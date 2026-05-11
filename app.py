from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render Deployment!"

if __name__ == '__main__':
    app.run()