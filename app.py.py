from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/network/status')
def status():
    return jsonify({
        "device": "Router-Core-01",
        "status": "online",
        "uptime": "99.99%",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Ejecuta la app en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
