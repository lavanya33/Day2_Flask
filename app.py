from flask import Flask #importing the module

app = Flask(__name__)   #creating instance of flask class and calling it app

@app.route("/")
def home():
    return "This is my first flask application"

if __name__ == "__main__":
    app.run(debug=True)