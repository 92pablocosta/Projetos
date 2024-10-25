from flask import request
from database.database import Info, Usuario

def usuario_request(id):
    usuario = Usuario.query.get(id)
    return usuario

def info_request(id):
    info = Info.query.get(id)
    return info