from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, HiddenField, IntegerField
from wtforms.validators import InputRequired, Email, EqualTo, Length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Đăng nhập')


class RegisterForm(FlaskForm):
    fullname = StringField('Họ và tên', validators=[InputRequired()])
    phone_number = StringField('Số điện thoại', validators=[InputRequired(), Regexp(regex=r'(84|0[3|5|7|8|9])+([0-9]{8})\b', message="Số điện thoại không hợp lệ")])
    email = EmailField('Email', validators=[InputRequired(), Email(message="Email không hợp lệ")])
    username = StringField('Username', validators=[InputRequired(), Length(min=8, max=50)])
    password = PasswordField('Mật khẩu', validators=[InputRequired(), Length(min=8, max=50), EqualTo('confirm', message='Hai mật khẩu không trùng khớp')])
    confirm = PasswordField('Xác nhận mật khẩu')
    register = SubmitField('Đăng ký')

class ForgetPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email(message="Email không hợp lệ")])
    confirm = SubmitField('Xác nhận')

class ConfirmOTPForm(FlaskForm):
    otp = StringField('Mã OTP', validators=[InputRequired()])
    confirm = SubmitField('Xác nhận')

class ChangePasswordForm(FlaskForm):
    password = PasswordField('Mật khẩu mới', validators=[InputRequired(), Length(min=8, max=50), EqualTo('confirm_password', message='Hai mật khẩu không trùng khớp')])
    confirm_password = PasswordField('Xác nhận mật khẩu')
    confirm = SubmitField('Xác nhận')

class EditForm(FlaskForm):
    fullname = StringField('Họ và tên', validators=[InputRequired()])
    phone_number = StringField('Số điện thoại', validators=[InputRequired(), Regexp(regex=r'(84|0[3|5|7|8|9])+([0-9]{8})\b', message="Số điện thoại không hợp lệ")])
    email = EmailField('Email', validators=[InputRequired(), Email(message="Email không hợp lệ")])
    confirm = SubmitField('Xác nhận')