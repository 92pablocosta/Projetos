from . import db

class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False) #procurar achar criptgrafia por aq
    tipo_usuario = db.Column(db.String(100), nullable=False)

class Usuario(Info):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)




class Admin(Info):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    nome_responsavel = db.Column(db.String(100), unique=False, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)
    capacidade_maxima_lot = db.Column(db.String(100), unique=False, nullable=False)
    CEP = db.Column(db.String(100), unique=False, nullable=False)
    logradouro = db.Column(db.String(100), unique=False, nullable=False)
    cidade = db.Column(db.String(100), unique=False, nullable=False)
    

class Prop(Info):
    __tablename__ = 'propaganda'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    responsavel = db.Column(db.String(100), unique=False, nullable=False)
    razao_social = db.Column(db.String(100), unique=False, nullable=False)
    CNPJ = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)
    tipo_veiculo = db.Column(db.String(100), unique=False, nullable=False)
    caracteristica_veiculo = db.Column(db.String(100), unique=False, nullable=False)

class Patro(Info):
    __tablename__ = 'patrocinador'
    id = db.Column(db.Integer, db.ForeignKey('info.id'), primary_key=True)
    nome_empresa = db.Column(db.String(100), unique=False, nullable=False)
    nome_responsavel = db.Column(db.String(100), unique=False, nullable=False)
    CNPJ = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(100), unique=False, nullable=False)

class Shows(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False)
    imagem = db.Column(db.LargeBinary, nullable=False)

class MeusShows(db.Model):
    __tablename__ = 'meus_shows'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)
    
    show = db.relationship('Shows', backref='meus_shows', lazy=True)
    
