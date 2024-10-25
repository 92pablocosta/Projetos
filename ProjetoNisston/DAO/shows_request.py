from flask import request
from database.database import Shows

def shows_request():
    page = request.args.get('page', 1, type=int)
    per_page = 6 
    shows = Shows.query.paginate(page=page, per_page=per_page)
    return shows

def show_especifico_request(show_id):
    show_especifico = Shows.query.get(show_id)
    return show_especifico