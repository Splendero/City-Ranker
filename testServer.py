from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return jsonify({"message": "Received data", "data": data})

if __name__ == "__main__":
    app.run(debug=True)