from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Путь к файлу, где будут сохраняться данные
file_path = "client_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    # Сохраняем данные в файл
    with open(file_path, "a") as f:
        f.write(f"Client Data: {data}\n")
    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
