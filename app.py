from flask import Flask, request, jsonify
from flask_cors import CORS  # Импортируем CORS

app = Flask(__name__)

# Разрешаем CORS для всех доменов (можно ограничить список доменов)
CORS(app)

# Список для хранения данных от пользователей
data_storage = []

@app.route('/')
def home():
    return "Welcome to the Flask Server!"

@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные от клиента
    user_data = request.json  # данные в формате JSON
    data_storage.append(user_data)
    
    # Возвращаем подтверждение
    return jsonify({"status": "success", "data": user_data}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    # Отправляем сохраненные данные обратно клиенту
    return jsonify({"data": data_storage}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
