import json
from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.contrib import messages
import stripe # 決済サービスのStripe

from base.models import Item, Order


# StripeのAPIキーを取得(settings.pyより)
stripe.api_key = settings.STRIPE_API_SECRET_KEY

# 税を定義
tax_rate = stripe.TaxRate.create(
    display_name='消費税',
    description='消費税',
    country='JP',
    jurisdiction='JP',
    percentage=settings.TAX_RATE * 100,
    inclusive=False, # 外税を指定(内税の場合はTrue)
)

class PaySuccessView(LoginRequiredMixin, TemplateView):
    """ 購入確定時の処理
    ※カート画面
    """
    template_name = 'pages/success.html'
    
    def get(self, request, *args, **kwargs):
        """
        """
        # checkout_sessionで渡したクエリを取得
        order_id = request.GET.get('order_id')
        # idと現userでOrderオブジェクトのListを取得する
        orders = Order.objects.filter(user=request.user, id=order_id)
        # もし要素数が1でなければ以降に進めないようにここでreturn
        if len(orders) != 1:
            # 好みでリダイレクトやメッセージを表示してあげてもいい
            return super().get(request, *args, **kwargs)
        
        # 1つの要素を変数へ代入
        order = orders[0]
        # 既にis_confirmed=Trueなら以降に進まないようにここでreturn
        if order.is_confirmed:
            # 好みでリダイレクトやメッセージを表示してあげてもいい
            return super().get(request, *args, **kwargs)

        order.is_confirmed = True # 注文確定に変更する
        order.save()

        # cart情報の削除(セッションの削除)
        if 'cart' in request.session:
            del request.session['cart']

        return super().get(request, *args, **kwargs)


class PayCancelView(LoginRequiredMixin, TemplateView):
    """ 購入キャンセル時の処理
    ※カート画面
    """
    template_name = 'pages/cancel.html'

    def get(self, request, *args, **kwargs):
        """
        """
        # 現userの仮Orderオブジェクトのリストを取得
        orders = Order.objects.filter(user=request.user, is_confirmed=False)

        for order in orders:
            # 在庫数と販売数を元の状態に戻す
            for elem in json.loads(order.items):
                item = Item.objects.get(pk=elem['pk'])
                item.sold_count -= elem['quantity']
                item.stock += elem['quantity']
                item.save()
        # 仮オーダーを全て削除
        orders.delete()

        return super().get(request, *args, **kwargs)


def create_line_item(unit_amount, name, quantity):
    """
    """
    return {
        'price_data': {
            'currency': 'JPY',
            'unit_amount': unit_amount,
            'product_data': {'name': name,}
        },
        'quantity': quantity,
        'tax_rates': [tax_rate.id]
    }


def check_profile_filled(profile):
    """ ユーザーの個人情報チェック
    住所などが未記入の場合は、購入しても発送ができない
    """
    if profile.name is None or profile.name == '':
        return False
    elif profile.zipcode is None or profile.zipcode == '':
        return False
    elif profile.prefecture is None or profile.prefecture == '':
        return False
    elif profile.city is None or profile.city == '':
        return False
    elif profile.address1 is None or profile.address1 == '':
        return False
    
    return True


class PayWithStripe(LoginRequiredMixin, View):
    """ 決済処理
    """
    def post(self, request, *args, **kwargs):
        """
        """
        # profileが埋まっているかどうか確認
        if not check_profile_filled(request.user.profile):
            messages.error(self.request, '配送の為、プロフィールを埋めてください。')
            return redirect('/profile/')

        # カート情報を取得
        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            messages.error(self.request, 'カートが空です。')
            return redirect('/')
        
        items = [] # Orderモデル用に追記
        line_items = []
        # カートに入っているアイテムを取得する
        for item_pk, quantity in cart['items'].items():
            item = Item.objects.get(pk=item_pk)
            line_item = create_line_item(item.price, item.name, quantity)
            line_items.append(line_item)

            # Orderモデル用に追記
            items.append({
                'pk': item.pk,
                'name': item.name,
                'image': str(item.image),
                'price': item.price,
                'quantity': quantity,
            })

            # 在庫をこの時点で引いておく。注文キャンセルの場合は在庫を戻す。
            # 販売数も加算しておく。
            item.stock -= quantity
            item.sold_count += quantity
            item.save()
        
        # 仮注文を作成(is_confirmed=False)※修正済み
        order = Order.objects.create(
            user=request.user,
            uid=request.user.pk,
            items=json.dumps(items),
            shipping=serializers.serialize("json", [request.user.profile]),
            amount=cart['total'],
            tax_included=cart['tax_included_total']
        )
        
        # Stripe
        checkout_session = stripe.checkout.Session.create(
            customer_email=request.user.email,
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            # success_urlには、クエリで注文IDを渡しておく
            success_url=f'{settings.MY_URL}/pay/success/?order_id={order.pk}',
            cancel_url=f'{settings.MY_URL}/pay/cancel/',
            )
        
        return redirect(checkout_session.url)
