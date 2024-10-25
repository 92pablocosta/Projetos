from flask import Flask
from route.login import login
from route.register_admin import register_admin
from route.register_patro import register_patro
from route.register_user import register_user
from route.register_prop import register_prop
from route.register_options import register_options
from route.forgot_password import forgot_password
from route.index_usuario import index_usuario
from route.index_gerenciamento import index_gerenciamento
from route.index_user_config import index_user_config
from route.index_show_interface import index_show_interface
from route.pagamento_tela import pagamento_interface
from database import init_app, db  

app = Flask(__name__)

#temporary secret key set in main without an environment variable.
app.secret_key = '3dcdaf74c8761209363e9a75450ba5b0'

#seuUsuario:suaSenha
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/teste_crescent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

app.register_blueprint(login)
app.register_blueprint(index_gerenciamento)
app.register_blueprint(index_usuario)
app.register_blueprint(register_user)
app.register_blueprint(register_prop)
app.register_blueprint(register_admin)
app.register_blueprint(register_patro)
app.register_blueprint(register_options)
app.register_blueprint(index_show_interface)
app.register_blueprint(forgot_password)
app.register_blueprint(index_user_config)
app.register_blueprint(pagamento_interface)
#app.register_blueprint(change_password)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
