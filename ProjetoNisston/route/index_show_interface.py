from flask import redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_integridade_token, verificar_session
from DAO.shows_request import show_especifico_request
from database.database import db, Shows

index_show_interface = Blueprint('index_show_interface', __name__)

@index_show_interface.route('/index/meus/<int:show_id>', methods = ['GET'])
def index_show_interface_generator(show_id):
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        show_especifico = show_especifico_request(show_id)

        return render_template('interface_shows.html', show_especifico=show_especifico)

    except Exception as ex:
        print(f'Erro104 {ex}')
        return redirect(url_for('login.login_generator'))