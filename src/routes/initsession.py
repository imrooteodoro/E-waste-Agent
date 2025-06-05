from controllers.sessioncontroller import SessionController
from flask import Response
from typing import Tuple

def initsession(app):
    @app.route('/session', methods=['GET'])
    def connectsession() -> Tuple[Response, int]:
        response = SessionController.session_trap()
        return  response