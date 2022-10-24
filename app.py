from flask import Flask
app=Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome</h1>'

@app.route('/new')
def new():
    return '<h1> hi welcome to new page</h1>'

app.run()