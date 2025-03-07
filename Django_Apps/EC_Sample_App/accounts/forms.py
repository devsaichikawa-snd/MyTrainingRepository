from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import Users


class RegisterForm(forms.ModelForm):
    """ 会員登録用のフォーム
    """
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'age', 'email', 'password']

    def save(self, commit=False):
        """ Passwordの暗号化処理
        """
        # オブジェクト化
        user = super().save(commit=False)
        # パスワードのValidation
        validate_password(self.cleaned_data['password'], user)
        # パスワードの暗号化
        user.set_password(self.cleaned_data['password'])
        # ユーザーの保存
        user.save()

        return user


class UserLoginForm(AuthenticationForm):
    """ ログイン用のフォーム
    """
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)

# class UserLoginForm(forms.Form):
#     """ ログイン用のフォーム パターン２
#     """
#     email = forms.EmailField(label='メールアドレス')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
