import os
from django.utils.crypto import get_random_string # ランダムに文字列を生成する

from django.db import models


def create_id():
    """ ランダムな22文字の文字列を生成する
    """
    return get_random_string(22)


def upload_image_to(instance, filename):
    item_id = instance.id
    return os.path.join('static', 'items', item_id, filename)


class Tag(models.Model):
    """ タグモデル
    """
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Category(models.Model):
    """ カテゴリモデル
    """
    slug = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    """ 商品モデル
    """
    id = models.CharField(default=create_id, primary_key=True, 
        max_length=22, editable=False) # ID
    name = models.CharField(default='', max_length=50) # 商品名
    price = models.PositiveIntegerField(default=0) # 価格 0以上の整数
    stock = models.PositiveIntegerField(default=0) # 在庫数 0以上の整数
    description = models.TextField(default='', blank=True) # 説明 空白許容
    sold_count = models.PositiveIntegerField(default=0) # 販売数 0以上の整数
    is_published = models.BooleanField(default=False) # 商品登録判定(登録済みか否か)
    created_at = models.DateTimeField(auto_now_add=True) # 作成日時
    update_at = models.DateTimeField(auto_now=True) # 更新日時
    image = models.ImageField(default='', blank=True,
        upload_to=upload_image_to) # 画像
    category = models.ForeignKey(Category,
        on_delete=models.SET_NULL, null=True, blank=True) # 外部キー
    tags = models.ManyToManyField(Tag) # タグ


    def __str__(self):
        """ Pythonデフォルトのクラスメソッド
        selfとはクラスのインスタンス
        strを返す※returnは文字列であること
        Return:
            Itemクラスの「name」
        """
        return self.name



