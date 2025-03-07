import datetime
from django.contrib.auth import get_user_model

from django.db import models


def custom_timestamp_id():
    """ 注文履歴テーブルのIDを生成する。
    タイムスタンプをIDにする
    マイクロ秒までとれるので、被ることはない
    """
    dt = datetime.datetime.now()
    return dt.strftime('%Y%m%d%H%M%S%f')


class Order(models.Model):
    """ 注文履歴モデル
    """
    id = models.CharField(default=custom_timestamp_id,
        editable=False, primary_key=True, max_length=50) # タイムスタンプ形式
    user = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE) # 外部キー(User.id)
    uid = models.CharField(editable=False, max_length=50) # user.id
    is_confirmed = models.BooleanField(default=False) # 決済の確定判定
    amount = models.PositiveIntegerField(default=0) # 料金(税抜)
    tax_included = models.PositiveIntegerField(default=0) # 料金(税込)
    items = models.JSONField()
    shipping = models.JSONField()
    shipped_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.id


