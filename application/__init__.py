# application/__init__.py
from mailing.sender import email_sender
from flask import Flask, jsonify, request
from scheduling.cron_jobs import main_fn
from threading import Thread
from datetime import datetime
import os


thread = Thread(target=main_fn)
thread.daemon = True
thread.start()
    

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
        return jsonify({'time': datetime.now()}), 200


    @app.route('/var')
    def print_var():
        return jsonify({"debug": app.debug,
                        'os_env': os.environ.get('WERKZEUG_RUN_MAIN')})
    
    @app.route('/email')
    def send_email():
        email_sender()
        return jsonify({'message': 'success'}), 200

    return app

app = create_app()
