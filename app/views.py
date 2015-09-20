from app import app
from flask import render_template, jsonify


@app.route('/', methods=['GET'])
def index():
    name = None # TODO get a name
    return render_template('base.html', name=name)


@app.route('/health', methods=['GET'])
def health():
    return 'OK ;)', 200


@app.route('/color', methods=['GET'])
def color():
    import random
    col = "#%06x" % random.randint(0, 0xFFFFFF)
    return jsonify({'color': col}), 200
