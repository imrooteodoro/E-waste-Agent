import os
from dotenv import load_dotenv


def authenticate() -> str: 
    keypass = os.getenv('api_key')
    return keypass