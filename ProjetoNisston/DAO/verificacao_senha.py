from database.database import Info

def confirmar_senha(email, senha):
    user = Info.query.filter_by(email=email).first()

    if not user:
        return None

    if user.senha == senha:
        return user.id
    else:
        return None
    
def tipo_sessao(id):
    user = Info.query.filter_by(id=id).first()
    
    return user.tipo_usuario