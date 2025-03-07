from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import UserActivateTokens
from . import forms


def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    register_form = forms.RegisterForm(request.POST or None)
    
    if register_form.is_valid():
        try:
            register_form.save()
            return redirect('accounts:home')
        except ValidationError as e:
            register_form.add_error('password', e)
    
    return render(request, 'accounts/register.html',
                context={'register_form': register_form, })


def activate_user(request, token):
    user_activate_token = UserActivateTokens.objects.activate_user_by_token(token)
    return render(
        request, 'accounts/activate_user.html')


def user_login(request):
    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, '正常にログインをしました。')
                return redirect('accounts:home')
            else:
                messages.warning(request, 'ユーザーがアクティブではありません。')
        else:
            messages.warning(request, 'メールアドレスかパスワードが間違っています。')
    return render(request, 'accounts/user_login.html',
                context={'login_form': login_form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'ログアウトしました。')
    return redirect('accounts:home')


@login_required
def user_edit(request):
    user_edit_form = forms.UserEditForm(
        request.POST or None, request.FILES or None, instance=request.user)
    if user_edit_form.is_valid():
        messages.success(request, '更新されました。')
        user_edit_form.save()
    return render(request, 'accounts/user_edit.html',
                context={'user_edit_form': user_edit_form})


@login_required
def change_password(request):
    change_password_form = forms.PasswordChangeForm(
        request.POST or None, instance=request.user)
    if change_password_form.is_valid():
        try:
            change_password_form.save()
            messages.success(request, 'パスワードが更新されました。')
            update_session_auth_hash(request,request.user)
        except ValidationError as e:
            change_password_form.add_error('password', e)
    
    return render(request, 'accounts/change_password.html',
                context={'change_password_form': change_password_form})



def show_error_page(request, exception):
    return render(request, '404.html')
