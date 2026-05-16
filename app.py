from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    app.run(debug=True)