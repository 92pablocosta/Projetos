from flask import Flask, redirect, render_template, Blueprint, url_for, session, request
from database.database import db, Prop

register_prop = Blueprint('register_prop', __name__)

@register_prop.route('/register_propaganda', methods = ['GET'])
def register_prop_generator():

    return render_template('register_prop.html')

@register_prop.route('/register_propaganda', methods = ['POST'])
def register_prop_form():
    print('aaaa')
    nome = request.form.get('nome')
    print('sdsd')
    responsavel = request.form.get('responsavel')
    razao_social = request.form.get('razao_social')
    CNPJ = request.form.get('CNPJ')
    email = request.form.get('email')
    telephone = request.form.get('telefone')
    veiculo_info = request.form.get('veiculo_info')
    caracteristica = request.form.get('caracteristica')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        print('aaaa')
        return redirect(url_for('register_prop.register_prop_generator'))
    
    print('aquia')
    novo_usuario = Prop(
        nome = nome,
        responsavel = responsavel,
        razao_social = razao_social,
        CNPJ = CNPJ,
        telefone = telephone,
        tipo_veiculo = veiculo_info,
        caracteristica_veiculo = caracteristica,
        email = email,
        senha = password,
        tipo_usuario="patrocinador"
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect(url_for('login.login_generator'))