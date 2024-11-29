from session.session import SessionGen
from flask import jsonify

class SessionController:
    def __init__():
        pass
    def session_trap():
        try:
            response = SessionGen.create_session()
            return jsonify({"session_id": response}), 200
        except:
            return jsonify({"error: Não foi possivel criar uma sessão"}), 500
        