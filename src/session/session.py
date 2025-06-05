import os
from flask import session

class SessionGen:
    @staticmethod
    def create_session() -> str:
        if  'user_id' not in session:
            session['user_id'] = os.urandom(16).hex()
        return session['user_id']
    @staticmethod
    def check_session() -> str:
        if 'user_id' in session:
             return session['user_id']
        else:
            return "Sessão não encontrada"
           
       