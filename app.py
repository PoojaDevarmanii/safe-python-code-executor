import os
import subprocess
import tempfile
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='static', static_url_path='/static')
print("STATIC FOLDER:", app.static_folder)
print("CURRENT WORKING DIR:", os.getcwd())

# ---------- Serve UI ----------
@app.route("/")
def home():
    return app.send_static_file("index.html")


# ---------- Code Execution Endpoint ----------
@app.route("/run", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    try:
        # Run inside Docker
        cmd = [
            "docker", "run",
            "--rm",
            "-v", f"{tmp_path}:/code.py",
            "python:3.11-slim",
            "python", "/code.py"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        output = result.stdout or result.stderr
        return jsonify({"output": output})

    finally:
        os.remove(tmp_path)


if __name__ == "__main__":
    print("STATIC FOLDER:", app.static_folder)
    app.run(debug=True)
