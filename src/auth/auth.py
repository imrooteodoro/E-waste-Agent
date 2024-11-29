import os
from dotenv import load_dotenv


def authenticate():
    keypass = os.getenv('api_key')
    return keypass