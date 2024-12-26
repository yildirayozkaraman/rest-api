from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/carp', methods=['POST'])
def carp():
    data = request.get_json()
    try:
        a = int(data.get('a'))
        b = int(data.get('b'))
        sonuc = a * b
        return jsonify({'sonuc': sonuc})
    except (TypeError, ValueError):
        return jsonify({'error': 'Lütfen geçerli iki sayı girin!'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=27)