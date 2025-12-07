from flask import Flask, jsonify, request
import socket
import requests
import os
import time

app = Flask(__name__)

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:5001/user")

start_time = time.time()


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/order")
def order():
    user_name = request.args.get("user", "Guest")
    try:
        r = requests.get(USER_SERVICE_URL, params={"name": user_name}, timeout=2)
        user_data = r.json()
    except Exception as e:
        user_data = {"error": str(e)}

    return jsonify(
        {
            "order_id": "ORD-12345",
            "status": "created",
            "user_info": user_data,
            "host": socket.gethostname(),
        }
    )


@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time
    return jsonify({"uptime_seconds": uptime})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
