from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        try:
            number = int(request.form['user_value'])
            result = "Even" if number % 2 == 0 else "oven"
            return f"Number is {result}"
        except ValueError as e:
            return f"Error is {e}, please check documentation"
    return '''
    <form method="POST">
    Enter number <input type="text" name="user_value" />
    <input type="submit" value="Check" />
    </form>
    '''


if __name__ == "__main__":
    app.run()