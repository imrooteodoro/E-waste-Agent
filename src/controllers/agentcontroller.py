from services.botservices import BotService
from flask import request, jsonify
from models.system_superprompt.prompt import final_prompt

class AgentController:
    def __init__(self):
        pass

    @staticmethod
    def send_message():
        try:
            data = request.get_json()
            user_message = data['user_message']
            system_context = final_prompt()
            bot_response = BotService.connect_agent(system_context, user_message)
            return jsonify({"bot_response": bot_response}), 200
        except Exception as e:
            return jsonify({"Error": f"Não foi possível enviar a mensagem: {str(e)}"}), 400
