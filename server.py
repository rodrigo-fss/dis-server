import os
from time import sleep

from flask import abort
from wtforms import SelectField
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, redirect, request, jsonify

from config.flask_vars import Config
from config.init_flask_celery import make_celery, make_db_connection


# Declare Flask app
application = Flask(__name__)
application.config.from_object(Config)


application.config['CELERY_BROKER_URL'] = "redis://redis:6379/0"
application.config['CELERY_RESULT_BACKEND'] = "redis://redis:6379/0"
celery = make_celery(application)
connection = make_db_connectio()


@application.route('/create_user', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    username = request.json['username']
    password = generate_password_hash(request.json['password'])

    insert_user_query = """ INSERT INTO dis.users (name, password)
    VALUES ({},{})""".format(username, password)
    cursor.execute(insert_user_query)
    connection.commit()

    return jsonify({'Usuario inserido com sucesso': username}), 201


@application.route('/check_user', methods=['POST'])
def check_user():
    if not request.json or 'title' not in request.json:
        abort(400)
    username = request.json['username']
    password = request.json['password']

    print(username, password)
    return jsonify({'task': task}), 201


@application.route('/pull_state/<task_id>', methods=['GET'])
def pull_state(task_id):
    """ Sends task status """
    task = convert_files.AsyncResult(task_id)
    response = {"state": task.state}
    return jsonify(response)


@celery.task(name='server.convert_files')
def convert_files(params):
    # Download from cloud storage
    path_list = []


def __handle_form(form):
    return {"bank_option": bank_option, "pdf_list": pdf_list}

if __name__ == '__main__':
    application.run(host='0.0.0.0', threaded=True)
