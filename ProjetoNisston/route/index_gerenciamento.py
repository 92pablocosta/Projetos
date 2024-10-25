from flask import redirect, render_template, Blueprint, url_for, request, send_file
from database.database import db, Shows
import io

index_gerenciamento = Blueprint('index_gerenciamento', __name__)

@index_gerenciamento.route('/index/gerenciamento', methods = ['GET'])
def index_gerenciamento_generator():
    return render_template('index_main_gerenciamento.html')

@index_gerenciamento.route('/index/gerenciamento', methods=['POST'])
def index_gerenciamento_form():
    name = request.form.get('title')
    local = request.form.get('local')
    descricao = request.form.get('description')
    preco = request.form.get('preco')
    quantidade = request.form.get('quantidade')
    data = request.form.get('data')
    img_file = request.files.get('url_img')
    
    img = img_file.read()

    novo_show = Shows(
        title=name,
        local=local,
        description=descricao,
        preco=preco,
        quantidade=quantidade,
        data=data,
        imagem=img
    )

    db.session.add(novo_show)
    db.session.commit()
    
    return redirect(url_for('index_gerenciamento.index_gerenciamento_generator'))

@index_gerenciamento.route('/show/imagem/<int:show_id>', methods = ['GET'])
def exibir_imagem(show_id):
    show = Shows.query.get(show_id)
    return send_file(io.BytesIO(show.imagem), mimetype='image/jpeg')