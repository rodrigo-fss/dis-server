import os

import psycopg2

from celery import Celery

def make_celery(app):
    """ The function creates a new Celery object, configures it with the
    broker from the application config, updates the rest of the Celery
    config from the Flask config and then creates a subclass of the
    task that wraps the task execution in an application context. """

    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)


    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery


def make_db_connection():
    connection = psycopg2.connect(user=os.environ['POSTGRES_USER'],
                                  password=os.environ['POSTGRES_PASSWORD'],
                                  host="postgres",
                                  port=os.environ['POSTGRES_PORT'],
                                  database="postgres")
    return connection
