from flask import Flask
from routes.index import index
from routes.sendmessage import send_to_bot
from routes.initsession import initsession
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(16).hex()

index(app)
send_to_bot(app)
initsession(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)