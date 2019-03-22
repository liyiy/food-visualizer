from flask import Flask, render_template, jsonify
from food_scraper import get_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/bullshit")
def bs():
    return render_template("/bs.html")

@app.route("/data")
def data():
    return jsonify(get_data("banana"))


if __name__ == "__main__":
    app.run(debug=True)
