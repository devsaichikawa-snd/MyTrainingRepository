from playhouse.db_url import connect
from peewee import Model
from peewee import IntegerField
from peewee import CharField
from flask_login import UserMixin


db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")



class User(UserMixin, Model):
    """ Userテーブルの定義
    ログイン認証の参照先にもなる
    """
    id = IntegerField(primary_key=True)  # ID, 数値
    name = CharField()  # 氏名, 文字列
    password = CharField()  # password, 文字列

    class Meta:
        database = db
        table_name = "User" # テーブル名

# 実行
db.create_tables([User])
