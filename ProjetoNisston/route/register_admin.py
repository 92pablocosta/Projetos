from flask import Flask, redirect, render_template, Blueprint, url_for, session

register_admin = Blueprint('register_admin', __name__)

@register_admin.route('/register_admin', methods = ['GET'])
def register_admin_generator():
    return render_template('register_admin.html')

@register_admin.route('/register_admin', methods = ['POST'])
def register_admin_form():
    
    return redirect(url_for('login.login_generator'))