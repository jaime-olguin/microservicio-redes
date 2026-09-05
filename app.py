from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/network/status')
def status():
    return jsonify({
        "device": "Router-Core-Principal-Santiago",
        "status": "online",
        "uptime": "99.99%",
        "version": "1.0.0"
    })

@app.route('/api/v1/network/interfaces')
def interfaces():
    return jsonify({
        "interfaces": [
            {"port": "GigabitEthernet0/0/0", "status": "up", "speed": "1000Mbps"},
            {"port": "GigabitEthernet0/0/1", "status": "down", "speed": "1000Mbps"}
        ]
    })

@app.route('/api/v1/network/ping/<host>')
def ping(host):
    return jsonify({
        "target": host,
        "status": "reachable",
        "latency_ms": 14.2
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
