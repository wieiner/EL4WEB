import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS  # Импортируем CORS

app = Flask(__name__)

# Разрешаем CORS для всех доменов (можно ограничить список доменов)
CORS(app)

# Список для хранения данных от пользователей
data_storage = []


# Строка подключения
# DATABASE_URL = 'postgres://username:password@hostname:port/database_name'
DATABASE_URL = 'postgresql://dbuser:AtoYdD3BlcCBHeSNARF70IO6lwGiza9r@dpg-ctt8t7pu0jms73bg7gr0-a/el4db'

# Функция для подключения к PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


@app.route('/')
def home():
    return "Welcome to the Flask Server!"

@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные от клиента
    user_data = request.json  # данные в формате JSON
    data_storage.append(user_data)

     # Подключаемся к базе данных
    conn = get_db_connection()
    cur = conn.cursor()

    # Вставляем данные в базу
    cur.execute('INSERT INTO user_inputs (input) VALUES (%s)', (user_data['input'],))
    conn.commit()

    cur.close()
    conn.close()

    # Возвращаем подтверждение
    return jsonify({"status": "success", "data": user_data}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    # Отправляем сохраненные данные обратно клиенту
    return jsonify({"data": data_storage}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

