import datetime
from time import sleep

import numpy as np
from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, jsonify

from config.flask_vars import Config
from config.init_flask_celery import make_celery, make_db_connection


# Declare Flask app
application = Flask(__name__)
application.config.from_object(Config)


application.config['CELERY_BROKER_URL'] = "redis://redis:6379/0"
application.config['CELERY_RESULT_BACKEND'] = "redis://redis:6379/0"
celery = make_celery(application)

connection = make_db_connection()
cursor = connection.cursor()


@application.route('/create_user', methods=['POST'])
def create_user():
    if not request.json:
        abort(400)
    username = request.json['username']
    email = request.json['email']
    password = generate_password_hash(request.json['password'])

    check_if_user_exist_query = """ SELECT * FROM dis.users
                                    WHERE email = '{}' """.format(email)
    cursor.execute(check_if_user_exist_query)
    user_with_same_nmae = cursor.fetchall()
    if user_with_same_nmae:
        return jsonify({'error': 'email already in use'})

    insert_user_query = """ INSERT INTO dis.users (name, email, password)
                            VALUES ('{}','{}', '{}')""".format(username,
                                                               email,
                                                               password)
    cursor.execute(insert_user_query)
    connection.commit()

    return jsonify({'sucess': 'user successfully inserted in the database'}), 201


@application.route('/check_user', methods=['POST'])
def check_user():
    if not request.json:
        abort(400)
    username = request.json['username']
    password = request.json['password']

    select_user_query = """ SELECT password FROM dis.users
                            WHERE name = '{}' """.format(username)

    cursor.execute(select_user_query)
    correct_password = cursor.fetchall()[0][0]

    if correct_password:
        if check_password_hash(correct_password, password):
            return jsonify({'sucess': 'right password'})  # return id
        else:
            return jsonify({'error': 'passwords dont match'})
    else:
        return jsonify({'error': 'user {} was not found'.
                        format(username)}), 201


@application.route('/create_image', methods=['POST'])
def create_image():
    if not request.json:
        abort(400)
    matrix = request.json['matrix']
    user = request.json['user_id']

    task = long_running_task.delay(user, matrix)
    return jsonify({'task_id': task.id})


@application.route('/pull_state/<task_id>', methods=['GET'])
def pull_state(task_id):
    """ Sends task status """
    task = long_running_task.AsyncResult(task_id)
    response = {"state": task.state}
    return jsonify(response)


@celery.task(name='server.long_running_task')
def long_running_task(user, matrix):
    init_time = datetime.datetime.now()
    for i in range(6):
        sleep(1)
    image = np.matrix(matrix)[:60, :60]
    image_size = image.shape
    iteration_number = i
    finish_time = datetime.datetime.now()

    insert_image_query = """ INSERT INTO dis.images (user_id, matrix, iterations,
        image_size, init_time, finish_time)
        VALUES ({},'{}',{},'{}','{}', '{}')""".format(user, image,
                                                      iteration_number,
                                                      image_size,
                                                      init_time, finish_time)

    cursor.execute(insert_image_query)
    connection.commit()


if __name__ == '__main__':
    application.run(host='0.0.0.0', threaded=True)
