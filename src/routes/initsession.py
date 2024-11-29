from controllers.sessioncontroller import SessionController

def initsession(app):
    @app.route('/session', methods=['GET'])
    def connectsession():
        response = SessionController.session_trap()
        print(response)
        return  response