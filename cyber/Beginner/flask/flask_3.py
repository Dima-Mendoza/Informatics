from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('template.html', title="main", message="Welcome!")

if __name__ == "__main__":
    app.run()