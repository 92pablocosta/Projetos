from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

# Configuração do Banco de Dados PostgreSQL
DATABASE_URL = "postgresql://postgres:pablo123@localhost/SlimeCastle"

# Criar conexão com o banco
engine = create_engine(DATABASE_URL)

# Criar sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar base para os modelos do banco
Base = declarative_base()

# Modelo do Slime no Banco de Dados
class Slime(Base):
    __tablename__ = "slimes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    nivel = Column(Integer)
    atk = Column(Integer)
    hp = Column(Integer)
    elemento = Column(String)

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Iniciar FastAPI
app = FastAPI()

# Dependência para conectar ao banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para adicionar um Slime ao banco de dados
@app.post("/slimes/")
def adicionar_slime(nome: str, nivel: int, atk: int, hp: int, elemento: str, db: Session = Depends(get_db)):
    novo_slime = Slime(nome=nome, nivel=nivel, atk=atk, hp=hp, elemento=elemento)
    db.add(novo_slime)
    db.commit()
    db.refresh(novo_slime)
    return {"mensagem": "Slime adicionado com sucesso!", "slime": novo_slime}

# Rota para listar todos os Slimes do banco de dados
@app.get("/slimes/")
def listar_slimes(db: Session = Depends(get_db)):
    return db.query(Slime).all()

# Rota para buscar um Slime pelo nome
@app.get("/slimes/{nome}")
def obter_slime(nome: str, db: Session = Depends(get_db)):
    slime = db.query(Slime).filter(Slime.nome == nome).first()
    if slime:
        return slime
    return {"erro": "Slime não encontrado"}

# Rota inicial
@app.get("/")
def home():
    return {"mensagem": "API do Slime Castle está rodando com PostgreSQL!"}
