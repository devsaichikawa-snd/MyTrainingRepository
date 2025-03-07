""" custom_context_processor.pyとは
今までの「context」変数は各Viewで実装し、HTML側に渡していた。
しかし、各Viewでの実装は冗長となるため、
「context」変数を一括で管理するファイルがコンテキストプロフェッサーとなる。
context変数 → htmlファイル内の{{ }}のような中で記載している変数
"""
from django.conf import settings

from base.models import Item


def base(request):
    """
    """
    items = Item.objects.filter(is_published=True)
    return {
        'TITLE': settings.TITLE,
        'ADDTIONAL_ITEMS': items,
        'POPULAR_ITEMS': items.order_by('-sold_count')
    }

