# Decorators

from flask import Flask, redirect, render_template, request, url_for

from db import DB

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html', context=DB().read())


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        DB().create(request.form.to_dict())
        return redirect(url_for('index'))


@app.get('/details/<id>')
def details(id):
    for user in DB().read():
        if user['id'] == id:
            data = user
    return render_template('details.html', data=data)


@app.route('/update/<id>', methods=('GET', 'POST'))
def update(id):
    db = DB().read()
    for user in db:
        if user['id'] == id:
            data = user
    if request.method == 'GET':
        return render_template('update.html', data=data)
    elif request.method == 'POST':
        db[db.index(data)].update(request.form.to_dict())
        DB().update(db)
        return redirect(url_for('index'))


@app.get('/delete/<id>')
def delete(id):
    db = DB().read()
    for item in db:
        if item['id'] == id:
            del db[db.index(item)]
    DB().update(db)
    return redirect(url_for('index'))
