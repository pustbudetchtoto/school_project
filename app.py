from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def page():
    return render_template('page.html')


if __name__ == '__main__':
    app.run()
