from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi!"

@app.route("/about")
def about():
    return "Flask is framerowk..."


if __name__ == "__main__":
    app.run()