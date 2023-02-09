import json
from . import forms
from . import auth
from .. import login_manager
from ..api.UserClient import UserClient
from flask import render_template, session, redirect, url_for, flash, request
from flask_login import current_user
from email.message import EmailMessage
import ssl, smtplib

def sendEmail(receiver, subject, content):
    em = EmailMessage()

    sender = 'phattran248vn@gmail.com'
    password = 'qszyapxgarbkajxk'

    em['From'] = 'WatchShop'
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(content)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())

@login_manager.user_loader
def load_user(user_id):
    return None

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            check_user = UserClient.does_exist(form)
            if check_user['message'] != 'valid':
                flash(check_user['message'], 'danger')
                return render_template('auth/register.html', form=form)
            else:
                user = UserClient.post_user_create(form)
                if user:
                    flash('Đăng ký thành công, mời đăng nhập', 'success')
                    return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = forms.LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            api_key = UserClient.post_login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                role_id = user['result']['role_id']
                if role_id == 1:
                    session['role'] = 'Admin'
                    return redirect(url_for('admin.home'))
                else:
                    session['role'] = 'Customer'
                    return redirect(url_for('main.home'))
            else:
                flash('Sai thông tin đăng nhập', 'danger')
        else:
            flash('Errors found', 'error')
    return render_template('auth/login.html', form=form)

@auth.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    form = forms.ForgetPasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form['email']
            otp = UserClient.create_OTP(email)
            session['email'] = email
            session['status'] = 'forgotpassword'
            if otp['message'] == False:
                flash('Email này không tồn tại hoặc chưa được đăng ký', 'danger')
                return redirect(url_for('auth.forgotpassword'))
            else:
                otp = otp['result']['id']
                session['otp'] = otp
                sendEmail(email, 'Mã OTP xác nhận thay đổi mật khẩu (hiệu lực 5 phút)', otp)
                flash('Vui lòng kiểm tra email để nhận mã OTP', 'success')
                return redirect(url_for('auth.confirm'))
    else:
        return render_template('auth/forgot_password.html', form=form)

@auth.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if session.get('status') is None:
        return redirect(url_for('main.home'))
    form = forms.ConfirmOTPForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            check_otp = UserClient.get_otp(form)
            if check_otp['message'] == 'Mã OTP đã hết hạn':
                session['newOTP'] = True
                flash(check_otp['message'] + ', vui lòng nhấn nút bên dưới để lấy lại mã', 'danger')
                return redirect(url_for('auth.confirm'))
            if check_otp['message'] == 'Mã OTP không chính xác':
                flash(check_otp['message'], 'danger')
                return redirect(url_for('auth.confirm'))
            else:
                session.pop('newOTP', None)
                flash('Mời nhập mật khẩu mới', 'success')
                return redirect(url_for('auth.changepassword'))
    else:
        return render_template('auth/confirm.html', form=form)

@auth.route('/changepassword', methods=['GET', 'POST'])
def changepassword():
    if session.get('status') is None:
        return redirect(url_for('main.home'))
    form = forms.ChangePasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_password = form.password.data
            UserClient.change_password(new_password, session['email'])
            session.pop('email', None)
            flash('Thay đổi mật khẩu thành công, mời đăng nhập lại', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Hai mật khẩu không trùng khớp', 'danger')
            return redirect(url_for('auth.changepassword'))
    else:
        return render_template('auth/change_password.html', form=form)

@auth.route("/newOTP", methods=['GET'])
def newOTP():
    otp = UserClient.create_OTP(session['email'])
    otp = otp['result']['id']
    sendEmail(session['email'], 'Mã OTP xác nhận thay đổi mật khẩu (hiệu lực 5 phút)', otp)
    flash('Vui lòng kiểm tra email để nhận mã OTP mới', 'success')
    return redirect(url_for('auth.confirm'))

@auth.route("/profile/edit", methods=['GET', 'POST'])
def edit_user():
    pass

@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
