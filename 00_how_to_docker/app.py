from flask import Flask

app = Flask("HelloApp")

@app.route("/")
def index():
    return "<h1>Hello World</h1>"
