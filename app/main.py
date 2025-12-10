```python
from flask import Flask, request, jsonify, render_template
from .agents import Planner

app = Flask(__name__)
planner = Planner()

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "multi-agent-zoology"}), 200

@app.route("/api/chat/<agent>", methods=["POST"])
def chat(agent):
    data = request.get_json(force=True, silent=True) or {}
    species_query = data.get("query", "").strip()
    # TODO: Add validation, caching, and conversation history handling
    result = planner.route(agent, species_query)
    return jsonify({"query": species_query, "result": result}), 200

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # TODO: Add proper prod server (e.g., gunicorn) and env config
    app.run(host="0.0.0.0", port=5000, debug=True)
```
