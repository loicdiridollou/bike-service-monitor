"""application/__init__.py"""
from threading import Thread
from datetime import datetime
import os
import yaml
from flask import Flask, jsonify, request, abort
from scheduling.cron_jobs import main_fn
from mailing.sender import email_sender


DEFAULT_CONFIG = "config/config.yaml"


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

    @app.route('/times')
    def list_times():
        with open("config/config.yaml", "rb") as config_file:
            cron_times = yaml.full_load(config_file)["cron_times"]
        return jsonify({"message": "success",
                        "times": cron_times}), 200

    @app.route('/times', methods=['POST'])
    def add_time(config_fn=DEFAULT_CONFIG):
        body = request.get_json()
        if body is None:
            abort(400)
        with open(config_fn, "rb", encoding="utf-8") as config_file:
            config_data = yaml.full_load(config_file)
        names = sorted(config_data["cron_times"].keys())
        new_num = int(names[-1][4:])+1
        config_data["cron_times"]["time" + str(new_num)] = body

        with open(config_fn, "w", encoding="utf-8") as config_file:
            yaml.dump(config_data, config_file)

        return jsonify({"message": "succes"}), 200

    @app.route("/times/<time_name>", methods=["DELETE"])
    def delete_times(time_name, config_fn=DEFAULT_CONFIG):
        with open(config_fn, "rb", encoding="utf-8") as config_file:
            config_data = yaml.full_load(config_file)
        names = config_data["cron_times"]
        if time_name not in names:
            abort(400)
        del config_data["cron_times"][time_name]

        with open(config_fn, "w", encoding="utf-8") as config_file:
            yaml.dump(config_data, config_file)

        return jsonify({"message": "succes", "deleted_time": time_name}), 200

    @app.errorhandler(400)
    def bad_request():
        return jsonify({'success': False,
                        'error': 400,
                        'message': 'bad request'
                        }), 400

    return app

application = create_app()
