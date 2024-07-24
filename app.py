from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    a = data['a']
    b = data['b']
    result = a + b
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
