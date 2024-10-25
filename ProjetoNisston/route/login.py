from flask import redirect, render_template, Blueprint, url_for, request, session
from DAO.verificacao_senha import confirmar_senha, tipo_sessao
import secrets

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def login_generator():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_form():
    email = request.form.get('email')
    senha = request.form.get('password')

    user_id = confirmar_senha(email, senha)

    if not user_id:
        return redirect(url_for('login.login_generator'))
    
    sessao_tipo = tipo_sessao(user_id)

    token = secrets.token_hex(16)
    session['token'] = token
    session['id_user'] = user_id

    print(sessao_tipo)
    if sessao_tipo == 'usuario':
        return redirect(url_for('index_usuario.index_usuario_generator'))
    else:
        return redirect(url_for('index_gerenciamento.index_gerenciamento_generator'))   

    