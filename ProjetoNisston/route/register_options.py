from flask import Flask, redirect, render_template, Blueprint

register_options = Blueprint('register_options', __name__)

@register_options.route('/register/options', methods = ['GET'])
def options_register():
    return render_template('register_options.html')
