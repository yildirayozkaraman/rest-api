from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/topla', methods=['GET'])
def topla():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        sonuc = a + b
        return jsonify({'sonuc': sonuc})
    except (TypeError, ValueError):
        return jsonify({'error': 'Lütfen geçerli iki sayı girin!'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=27)
