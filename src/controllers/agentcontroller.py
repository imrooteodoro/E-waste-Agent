from services.botservices import BotService
from flask import request, jsonify, Response
from models.system_superprompt.prompt import final_prompt
from typing import Tuple, Dict, Any

class AgentController:
    @staticmethod
    def send_message() -> Tuple[Response, int]:
        try:
            data:Dict[str, Any] = request.get_json()
            user_message: str = data['user_message']
            system_context :str = final_prompt()
            bot_response :str = BotService.connect_agent(system_context, user_message)
            return jsonify({"bot_response": bot_response}), 200
        except Exception as e:
            return jsonify({"Error": f"Não foi possível enviar a mensagem: {str(e)}"}), 400
