from controllers.agentcontroller import AgentController

def send_to_bot(app):
    @app.route('/message', methods=['POST'])
    def sendmessage():
        response = AgentController.send_message()
        return response