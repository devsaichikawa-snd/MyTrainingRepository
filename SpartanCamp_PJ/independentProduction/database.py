import datetime
from playhouse.db_url import connect
from peewee import Model
from peewee import IntegerField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField


db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class BaseModel(Model):
    class Meta:
        database = db


class UploadImages(BaseModel):
    id = IntegerField(primary_key=True)  # ID, 数値
    image_name = CharField(unique=True)  # 画像の名前, 文字列
    created_date = DateTimeField(default=datetime.datetime.now)  # 作成日時


class DetectResult(BaseModel):
    id = IntegerField(primary_key=True)  # ID, 数値
    uploadImages = ForeignKeyField(
        UploadImages, backref="uploadImages"
    )  # 外部キー(UploadImages)
    count = IntegerField()  # 検出結果の個数
    created_date = DateTimeField(default=datetime.datetime.now)  # 作成日時


db.create_tables([UploadImages])
db.create_tables([DetectResult])
