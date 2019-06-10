FROM python:3.7.3-slim-stretch

RUN apt-get update
RUN apt-get install -y software-properties-common poppler-utils
RUN apt-get update
RUN apt-get install -y  python-psycopg2 libpq-dev
RUN pip3 install redis celery requests psycopg2-binary
RUN pip3 install numpy flask flask_wtf gunicorn
RUN pip3 install pandas --upgrade pip

COPY ./ /usr/local/src/
WORKDIR /usr/local/src/

ENV PYTHONPATH=/usr/local/src/ 
EXPOSE 5000

CMD ["gunicorn", "-c", "config/wsgi.py", "server"]