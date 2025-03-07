import json
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Order


class OrderIndexView(LoginRequiredMixin, ListView):
    """ orders.htmlを返す
    """
    model = Order
    template_name = 'pages/orders.html'

    # 要素の並び替え(基準:created_at)、ListViewのオーバーライド
    ordering = '-created_at'

    def get_queryset(self):
        """ ログインユーザーの注文履歴だけを取得する
        """
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, DetailView):
    """ order.htmlを返す
    """
    model = Order
    template_name = 'pages/order.html'

    def get_queryset(self):
        """ ログインユーザーの注文履歴だけを取得する
        """
        return Order.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        # json to dict
        context["items"] = json.loads(obj.items)
        context["shipping"] = json.loads(obj.shipping)
        
        return context
