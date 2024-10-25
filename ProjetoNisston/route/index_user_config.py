from flask import redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_session, verificar_integridade_token
from DAO.user_request import usuario_request, info_request
index_user_config = Blueprint('index_user_config', __name__)

@index_user_config.route('/index/user/configuração', methods = ['GET'])
def index_user_config_generator():
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        usuario = usuario_request(id)
        info = info_request(id)

    except Exception as ex:
        print(f'erro13 {ex}')
        return redirect(url_for('login.login_generator'))

    return render_template('index_user_config.html', usuario=usuario, info=info) 