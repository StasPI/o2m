from random import choice

from flask import Flask, redirect, render_template, request, url_for

from custom.use_db import UseDB

app = Flask(__name__)

db = UseDB()

@app.after_request
def add_header(response):
    response.cache_control.max_age = 30
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'GET':
            return render_template('home.html')
        elif request.method == 'POST':
            return render_template('home.html',
                                   random_user=choice(db.all_users()))
        return render_template('home.html')
    except:
        return redirect(url_for('home'))


@app.route('/user/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    try:
        if request.method == 'delete':
            insert_username = request.form.get('insert_username')
            if insert_username != None:
                db.insert_user(insert_username)
        elif request.method == 'POST':
            delete_username = request.form.get('delete_username')
            if delete_username != None:
                db.delete_user(delete_username)
        return render_template("user.html", users=db.all_users())
    except:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()