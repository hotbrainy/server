
from flask import Flask, render_template, redirect, url_for, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, abort, redirect, flash, url_for
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail
from server.db.forms import LoginForm
from server.db.models import User


def init_authentication(app):
    # This function is connected to app
    login_manager = LoginManager()
    login_manager.login_view = 'not_logged_in'
    login_manager.init_app(app)
    csrf = CSRFProtect(app)
    mail = Mail(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # @app.route('/login', methods=['POST'])
    # def login_post():
    #     form = LoginForm(request.form)

    # @app.route('/logout')
    # @login_required
    # def logout():
    #     logout_user()
    #     return redirect(url_for('login_get'))


