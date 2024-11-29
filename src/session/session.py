import os
from flask import session

class SessionGen:
    def __init__(self):
        pass
    def create_session():
        # Cria uma nova sessão
        if  'user_id' not in session:
            session['user_id'] = os.urandom(16).hex()
        return session['user_id']
    
    def check_session():
        #verifica se a sessão existe
        if 'user_id' in session:
             return session['user_id']
        else:
            return "Sessão não encontrada"
           
       