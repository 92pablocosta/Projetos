from flask import Blueprint, render_template, request, redirect, url_for
from database.database import db, Usuario
#from utils.crypt import encriptografar

register_user = Blueprint('register_user', __name__)

@register_user.route('/register_user', methods=['GET'])
def register_user_generator():
    return render_template('register_user.html')

@register_user.route('/register_user', methods=['POST'])
def register_user_form():
    #pegar elemntos
    name = request.form.get('name')
    username = request.form.get('username')
    telephone = request.form.get('telephone')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    #verificar senha
    if password != confirm_password:
        return redirect(url_for('register_user.register_user_generator'))

    #classe para passar os parametros do usuario normal
    novo_usuario = Usuario(
        nome=name,
        username = username,
        telefone=telephone,
        email=email,
        senha=password,
        tipo_usuario="usuario"  
    )
    
    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('login.login_generator'))
