from flask import request, render_template, redirect, flash, g, url_for
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from nmhvoice import db
from nmhvoice.user import user
from models import User
from forms import SignInForm, SignUpForm

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@user.record_once
def on_load(state):
    login_manager.init_app(state.app)


@user.before_app_request
def before_request():
    g.user = current_user

@user.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        remember_me = form.remember_me.data
        this_user = User.query.filter_by(email=user_email).first()
        if this_user is not None or this_user.check_password(user_password) is True:
            login_user(this_user, remember=remember_me)
            flash('Successfully Logged In')
            return redirect(request.args.get('next') or '/')
        else:
            return "Login Failed"
    else:
        return "Login"
login_manager.login_view = "user.signin"


@user.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('index'))

@user.route('/signup', methods=['GET','POST'])
def signup():
    form=SignUpForm()
    if form.validate_on_submit():
        new_user = User(form.name.data,form.email.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Successfully Signed Up!")
        return redirect('/')
    return "Sign Up"
