from flask import Flask, request, jsonify, render_template
from ai import categorize

app = Flask(__name__)

# home page
@app.route("/")
def home():
    return render_template("index.html")

# results page
@app.route("/results")
def results():
    return render_template("results.html")

# this route takes an item and returns its category
@app.route("/add", methods=["POST"])
def add():
    item = request.json["item"]
    category = categorize(item)
    return jsonify({"item": item, "category": category})

if __name__ == "__main__":
    app.run(debug=True)
