""" バッチ処理
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """_summary_

    Args:
        BaseCommand (_type_): _description_
    """
    def handle(self, *args, **options):
        print('Storeのバッチ処理です')
