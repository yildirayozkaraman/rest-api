from flask import Flask, request, jsonify

# Flask uygulamasını oluşturuyoruz
app = Flask(__name__)

# GET endpoint: İki sayıyı toplama
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        # URL parametrelerinden sayıları alıyoruz
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 + num2
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide two numbers."}), 400

# POST endpoint: Sayıları çarpma
@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    try:
        # JSON gövdesinden sayıları alıyoruz
        data = request.get_json()
        numbers = data.get('numbers', [])
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError
        result = 1
        for num in numbers:
            result *= num
        return jsonify({"result": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide a list of numbers."}), 400

# Uygulamanın çalışacağı portu belirliyoruz
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27)
