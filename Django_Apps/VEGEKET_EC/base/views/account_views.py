from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
# LoginRequiredMixinとは、未ログインに対しての操作制御を行える
# 例えば、登録済みの情報は未ログイン者には見えないようにする

from base.models import Profile
from base.forms import UserCreationForm


class SignUpView(CreateView):
    """ 新規登録
    """
    form_class = UserCreationForm # ユーザー入力フォームの指定
    success_url = '/login/' # 登録後の遷移先
    template_name = 'pages/login_signup.html'

    def form_valid(self, form):
        """ フォームが有効だった場合の処理
        """
        messages.success(self.request,
            '新規登録が完了しました。続けてログインしてください。')
        return super().form_valid(form)


class Login(LoginView):
    """ ログイン
    """
    template_name = 'pages/login_signup.html'

    def form_valid(self, form):
        """ フォームが有効だった場合の処理
        """
        messages.success(self.request,
            'ログインしました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """ フォームが無効だった場合の処理
        """
        messages.error(self.request,
            'エラーでログインできません。')
        return super().form_invalid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """ ユーザーアカウント情報を更新
    ※ユーザーは登録済みであること
    """
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'

    def get_object(self):
        """
        """
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ ユーザー詳細情報更新
    ※ユーザーは登録済みであること
    """
    model = Profile
    template_name = 'pages/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
        'city', 'address1', 'address2', 'tel')
    success_url = '/profile/'

    def get_object(self):
        """
        """
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
