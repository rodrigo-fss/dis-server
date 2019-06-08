import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MhotAlGw_%*2<;B)'
