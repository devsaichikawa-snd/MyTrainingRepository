""" バッチ処理
"""
import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand

from ECConfig.settings import BASE_DIR # settings.py
from stores.models import Orders


class Command(BaseCommand):
    """ orderの履歴をバッチ処理で出力する
    """
    def add_arguments(self, parser):
        parser.add_argument('--user_id', default='all')
    
    
    def handle(self, *args, **options):
        """ 実行
        """
        orders = Orders.objects.all()
        user_id = options['user_id']
        if user_id == 'all':
            orders = orders.all()
        else:
            orders = orders.filter(user_id=user_id)
        
        file_path = os.path.join(
            BASE_DIR, 'output', 'orders', f'orders_{datetime.now().strftime("%Y%m%d%H%M%S")}')
        
        with open(file_path, mode='w', newline='\n', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'user', 'address', 'total_price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for order in orders:
                writer.writerow({
                    'id': order.id,
                    'user': order.user,
                    'address': order.address,
                    'total_price': order.total_price,
                })
