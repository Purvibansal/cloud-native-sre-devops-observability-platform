from flask import Flask, jsonify, request
import socket
import time
import random

app = Flask(__name__)

start_time = time.time()


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/user")
def user():
    username = request.args.get("name", "Guest")
    return jsonify(
        {
            "message": f"Hello, {username} from User Service!",
            "host": socket.gethostname(),
        }
    )


@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time
    return jsonify(
        {"uptime_seconds": uptime, "random_latency_ms": random.randint(10, 200)}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
