from flask import Flask, redirect, render_template, Blueprint, url_for, session

register_patro = Blueprint('register_patro', __name__)

@register_patro.route('/register_patro', methods = ['GET'])
def register_patro_generator():
    return render_template('register_patro.html')

@register_patro.route('/register_patro', methods=['POST'])
def register_patro_form():
    return None