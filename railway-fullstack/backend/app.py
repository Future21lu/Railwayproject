from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Connect to your database (PostgreSQL as an example)
DATABASE_URL = os.getenv('DATABASE_URL')  # Railway provides DATABASE_URL environment variable

def get_data_from_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM your_table_name;")  # Replace with your table and query
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

@app.route('/api/data', methods=['GET'])
def get_data():
    data = get_data_from_db()
    return jsonify(data)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
