from flask import jsonify, Response
from typing import Tuple

def index(app):
    @app.route('/about', methods=['GET'])
    def index_route()-> Tuple[Response, int] :
        about_message = 'Eletronic Waste Agent v1.0'
        return jsonify({"about_bot": about_message}), 200 