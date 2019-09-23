from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, jsonify, make_response, flash, session)

from flask_cors import CORS, cross_origin, logging


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Saturday'

# CORS.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0:5000/'

# cors = CORS(app, resources={r"/api/posts": {"origins": "http://localhost:5000"}})
#http://localhost:porT

@app.route('/', methods=['GET','POST', 'OPTIONS'])
def index():

    return render_template('index.html')


@app.route('/api/posts', methods=['GET','POST', 'OPTIONS'])
@cross_origin(origin='http://localhost:5000/',headers=['Content-Type','Authorization'])
# @cross_origin(origin="*")
def displays_posts():
    req = request.get_json()

    print(req, '!')
    # print(req['author'])

    res = jsonify(req)

    return res


if __name__ == "__main__":

    app.config['CORS_HEADERS'] = 'Content-Type'

    app.debug = True
    app.jinja_env.auto_reload = app.debug
    logging.getLogger('flask_cors').level = logging.DEBUG

    app.run(port=5000, host='0.0.0.0')
