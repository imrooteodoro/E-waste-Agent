from session.session import SessionGen
from flask import jsonify, Response
from typing import Tuple

class SessionController:
    @staticmethod
    def session_trap() -> Tuple[Response, int] :
        try:
            response: str = SessionGen.create_session()
            return jsonify({"session_id": response}), 200
        except:
            return jsonify({"error: Não foi possivel criar uma sessão"}), 500
        