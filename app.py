from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_price_comparison

app = Flask(__name__)
CORS(app)

@app.route("/compare")
def compare():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400
    result = get_price_comparison(query)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
