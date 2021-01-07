import os
from flask import Flask, redirect, render_template, request, url_for
import psycopg2
app = Flask(__name__)


def connect_db():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    return conn, cursor


def all_users():
    sql = 'select Name from random_user'
    users = []
    conn, cursor = connect_db()
    cursor.execute(sql)
    records = cursor.fetchall()
    for user in records:
        users.append(user[0])
    return users


def insert_user(insert_username):
    sql = 'insert into random_user (Name) values(\'' + str(
        insert_username) + '\')'
    conn, cursor = connect_db()
    cursor.execute(sql)
    conn.commit()


def delete_user(delete_username):
    sql = 'delete from random_user where Name = \'' + str(
        delete_username) + '\''
    conn, cursor = connect_db()
    cursor.execute(sql)
    conn.commit()


@app.after_request
def add_header(response):
    response.cache_control.max_age = 30
    return response


@app.route('/', methods=['GET'])
def home():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        return render_template('home.html')
    except:
        return redirect(url_for('home'))


@app.route('/user/', methods=['GET', 'POST'])
def user():
    try:
        if request.method == 'POST':
            insert_username = request.form.get('insert_username')
            delete_username = request.form.get('delete_username')
            if insert_username != None:
                insert_user(insert_username)
            elif delete_username != None:
                delete_user(delete_username)
        return render_template("user.html", users=all_users())
    except:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()