from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/crib")
def hello():
    return '<h1>Started from the botton now we here!</h1>'


@app.route("/about")
def about():
    return "<h1>Damn right you here!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
