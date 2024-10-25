from flask import Flask, redirect, render_template, Blueprint, url_for, session

forgot_password = Blueprint('forgot_password', __name__)

@forgot_password.route('/forgot_password', methods = ['GET'])
def forgot_password_generator():
    return render_template('forgot_password.html')