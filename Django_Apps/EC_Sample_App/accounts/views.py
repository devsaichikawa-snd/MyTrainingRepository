import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import RegisterForm, UserLoginForm


# ログのオブジェクト
application_logger = logging.getLogger('application-logger')


class HomeView(TemplateView):
    """ Home画面への遷移
    """
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        """
        """
        context = super().get_context_data(**kwargs)
        application_logger.debug('Home画面を表示します。')
        return context


class RegisterUserView(CreateView):
    """ ユーザー登録処理
    """
    template_name = 'register.html'
    form_class = RegisterForm


class UserLoginView(LoginView):
    """ ログイン処理
    """
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)

        return super().form_valid(form)


# class UserLoginView(FormView):
#     """ ログイン処理 パターン２
#     """
#     template_name = 'user_login.html'
#     form_class = UserLoginForm

#     def post(self, request, *args, **kwargs):
#         """ ログイン画面でのPost処理(「登録」ボタン処理)
#         """
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)

#         next_url = request.POST['next']

#         if user is not None and user.is_active:
#             login(request, user)
#         if next_url:
#             return redirect(next_url)
#         return redirect('accounts:home')


class UserLogoutView(LogoutView):
    """ ログアウト処理
    """
    pass


# class UserLogoutView(View):
#     """ ログアウト処理 パターン２
#     """
#     def get(self, request, *args, **kwargs):
#         """ ログアウトボタン押下時の処理
#         """
#         logout(request)
#         return redirect('accounts:user_login')


class UserView(LoginRequiredMixin, TemplateView):
    """
    """
    template_name = 'user.html'


    # 他のログイン未実施時のアクセス制御パターン
    # @method_decorator(login_required, name='dispatch') ⇒パターン2
    # class UserView(LoginRequiredMixin, TemplateView):
    #     template_name = 'user.html'

    #     @method_decorator(login_required) ⇒パターン1
    #     def dispatch(self, *args, **kwargs):
    #         return super().dispatch(*args, **kwargs)
    
    # パターン1:クラスにデコレーターを付与
    # パターン2:dispatchメソッドにデコレータを付けてオーバーライド
    
