from controllers.agentcontroller import AgentController
from flask import Response
from typing import Tuple

def send_to_bot(app):
    @app.route('/message', methods=['POST'])
    def sendmessage() -> Tuple[str, int]:
        response: str = AgentController.send_message()
        return response