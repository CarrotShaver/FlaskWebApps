import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Extra Text For Secret Key"