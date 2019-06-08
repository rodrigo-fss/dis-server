FROM tesseractshadow/tesseract4re

RUN apt-get update
RUN apt-get install -y python-psycopg2 software-properties-common
RUN apt-get install -y python3.6 python3-pip poppler-utils 
RUN apt install -y default-jdk
RUN pip3 install redis celery requests psycopg2
RUN pip3 install numpy flask flask_wtf gunicorn
RUN pip3 install pandas --upgrade pip

COPY ./ /usr/local/src/
WORKDIR /usr/local/src/

ENV PYTHONPATH=/usr/local/src/ 
EXPOSE 5000

CMD ["gunicorn", "-c", "config/wsgi.py", "server"]