from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    mssg="starting of testing"
    return mssg


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
