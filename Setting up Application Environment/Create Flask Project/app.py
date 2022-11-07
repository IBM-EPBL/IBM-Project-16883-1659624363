from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<name>')
def hello_name(name):
    return 'Hello'+" " + name


if __name__ == '__main__':
    app.run(debug=True)
