from flask import session

def verificar_session(token, id):
    if not token or not id:
        return False
    
#talvez nao necessario
def verificar_integridade_token(token, id):
    if token != session['token'] or id != session['id_user']:
        return False
    
#def verificar_tempo():