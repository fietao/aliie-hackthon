from flask import Flask, request, jsonify, render_template
from ai import categorize

app = Flask(__name__, template_folder="html")

# home page
@app.route("/")
def home():
    return render_template("firspage.html")

# results page
@app.route("/results")
def results():
    return render_template("result.html")

# this route takes an item and returns its category
@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)
    if not data or "item" not in data:
        return jsonify({"error": "missing item"}), 400
    item = data["item"]
    if not isinstance(item, str):
        return jsonify({"error": "item must be a string"}), 400
    item = item.strip()[:200]  # limit to 200 characters, no raw user data leaked
    if not item:
        return jsonify({"error": "item cannot be empty"}), 400
    category = categorize(item)
    return jsonify({"item": item, "category": category})

if __name__ == "__main__":
    app.run(debug=False)
