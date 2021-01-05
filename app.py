from flask import Flask
import os
import psycopg2
app = Flask(__name__)
 
 
@app.route('/')
def hello():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM random_user')
    records = cursor.fetchall()
    
    return records
 
if __name__ == '__main__':
    app.run()