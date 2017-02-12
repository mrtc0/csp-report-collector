from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
app = Flask(__name__)


@app.route('/')
def index():
    r = make_response(render_template('index.html'))
    r.headers["Content-Security-Policy"] = "default-src 'self'; report-uri http://localhost:8000/report/"
    return r


@app.route('/report', methods=['POST'])
def report():
    print(request.data)
    return ""


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
