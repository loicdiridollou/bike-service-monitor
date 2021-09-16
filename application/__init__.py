# application/__init__.py
from flask import Flask, abort, json, jsonify, request
from experiments.cron_jobs_test import main_fn
from threading import Thread
from datetime import datetime


def create_app(test_config=None):
    """Creating the app and db
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    @app.route('/')
    def home():
        return jsonify({'message': 'healthy'}), 200


    @app.route('/time')
    def print_time():
        return jsonify({'time': datetime.now()})

    thread = Thread(target=main_fn)
    thread.daemon = True
    thread.start()

    return app


app = create_app()