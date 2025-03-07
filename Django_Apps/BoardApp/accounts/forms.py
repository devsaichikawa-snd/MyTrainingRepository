from django import forms
from django.contrib.auth.password_validation import validate_password

from .models import Users


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model = Users
        fields = ('username', 'age', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean() # オブジェクト化
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります。')
    
    def save(self, commit=False):
        user = super().save(commit=False) # オブジェクト化
        # パスワードのValidation
        validate_password(self.cleaned_data['password'], user)
        # パスワードの暗号化
        user.set_password(self.cleaned_data['password'])
        user.save() # ユーザーの保存

        return user


class LoginForm(forms.Form):
    email = forms.CharField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    picture = forms.FileField(label='写真', required=False)
    
    class Meta:
        model = Users
        fields = ('username', 'age', 'email', 'picture')


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta():
            model = Users
            fields = ('password',)

    def clean(self):
        cleaned_data = super().clean() # オブジェクト化
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります。')
    
    def save(self, commit=False):
        user = super().save(commit=False) # オブジェクト化
        # パスワードのValidation
        validate_password(self.cleaned_data['password'], user)
        # パスワードの暗号化
        user.set_password(self.cleaned_data['password'])
        user.save() # ユーザーの保存

        return user
