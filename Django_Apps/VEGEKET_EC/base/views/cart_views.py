from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from collections import OrderedDict

from base.models import Item


class CartListView(LoginRequiredMixin, ListView):
    """
    """
    model = Item
    template_name = 'pages/cart.html'

    def get_queryset(self):
        """ ListViewクラスのget_querysetをOverride
        querysetとは →モデルに登録されたvalueのList
        """
        # cartセッションを取得
        cart = self.request.session.get('cart', None)
        # cartセッションの有無を確認する
        if cart is None or len(cart) == 0:
            return redirect('/')
        self.queryset = []
        self.total = 0
        for item_pk, quantity in cart['items'].items():
            obj = Item.objects.get(pk=item_pk)
            obj.quantity = quantity
            obj.subtotal = int(obj.price * quantity)
            self.queryset.append(obj)
            self.total += obj.subtotal
        self.tax_included_total = int(self.total * (settings.TAX_RATE + 1))
        cart['total'] = self.total
        cart['tax_included_total'] = self.tax_included_total
        self.request.session['cart'] = cart

        return super().get_queryset()


    def get_context_data(self, **kwargs):
        """ ListViewクラスのget_context_dataをOverride
        """
        # 親クラスのget_context_dataを実行し、結果を取得
        context = super().get_context_data(**kwargs)
        try:
            context['total'] = self.total
            context['tax_included_total'] = self.tax_included_total
        except Exception:
            pass
        
        return context



class AddCartView(LoginRequiredMixin, View):
    """
    """
    def post(self, request):
        """ item.htmlからPostされたときの処理
        """
        item_pk = request.POST.get('item_pk')
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', None) # cartのセッションを取得する。無ければNone
        
        # cartがNoneもしくは空の場合
        if cart is None or len(cart) == 0:
            items = OrderedDict() # index付きの辞書オブジェクト
            cart = {'items': items} # Key:'items'、value:itemsを定義(itemsはList)
        
        # itemsの中にitempkが含まれている場合
        if item_pk in cart['items']:
            cart['items'][item_pk] += quantity
        else:
            cart['items'][item_pk] = quantity
        request.session['cart'] = cart
        
        return redirect('/cart/')

    # # getメソッドではトップへリダイレクトする場合はこのようにかけます。
    # def get(self, request):
    #     return redirect('/')


@login_required # 未ログイン時は実行不可
def remove_from_cart(request, pk):
    """ cartの削除
    ※関数ビュー
    """
    cart = request.session.get('cart', None)
    if cart is not None:
        del cart['items'][pk]
        request.session['cart'] = cart
    
    return redirect('/cart/')

