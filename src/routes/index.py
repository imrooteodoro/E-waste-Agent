from flask import jsonify

def index(app):
    @app.route('/about', methods=['GET'])
    def index_route():
        about_message = 'Eletronic Waste Agent v1.0'
        return jsonify({"about_bot": about_message}) 