from django.db import models

from accounts.models import Users


class ProductTypes(models.Model):
    """ 製品種類テーブル
    """
    name = models.CharField(max_length=1000)

    class Meta:
        db_table = 'product_types'
    
    def __str__(self):
        return self.name


class Manufacturers(models.Model):
    """ 製品メーカーテーブル
    """
    name = models.CharField(max_length=1000)

    class Meta:
        db_table = 'manufacturers'
    
    def __str__(self):
        return self.name


class ProductsManager(models.Manager):
    """ 商品操作
    """
    def reduce_stock(self, cart):
        for item in cart.cartitems_set.all():
            update_stock = item.product.stock - item.quantity
            item.product.stock = update_stock
            item.product.save()


class Products(models.Model):
    """ 商品テーブル
    備忘録:「Manufacturer」は誤って大文字スタートになっている。
    """
    name = models.CharField(max_length=1000)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE)
    Manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)

    objects = ProductsManager()

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name


class ProductPictures(models.Model):
    """ 商品写真テーブル
    """
    picture = models.FileField(upload_to='product_pictures/')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        db_table = 'product_pictures'
        ordering = ['order'] # order_byの対象カラム
    
    def __str__(self):
        return self.product.name + ': ' + str(self.order)


class Carts(models.Model):
    """ カートテーブル
    """
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'carts'


class CartItemsManager(models.Manager):
    """ カート格納アイテムの操作
    """
    def save_item(self, product_id, quantity, cart):
        c = self.model(quantity=quantity, product_id=product_id, cart=cart)
        c.save()


class CartItems(models.Model):
    """ カート格納アイテムテーブル
    """
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)

    objects = CartItemsManager()

    class Meta:
        db_table = 'cart_items'
        unique_together = [['product', 'cart']]


class Addresses(models.Model):
    """ 住所テーブル
    """
    zip_code = models.CharField(max_length=8)
    prefecture = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'addresses'
        unique_together = [['zip_code', 'prefecture', 'address', 'user']]

    def __str__(self):
        return f'{self.zip_code} {self.prefecture} {self.address}'


class OrdersManager(models.Manager):
    """ 注文操作
    """
    def insert_cart(self, cart: Carts, address, total_price):
        return self.create(
            total_price=total_price,
            address=address,
            user=cart.user
            )


class Orders(models.Model):
    """ 注文テーブル
    """
    total_price = models.PositiveIntegerField()
    address = models.ForeignKey(Addresses, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)

    objects = OrdersManager()

    class Meta:
        db_table = 'orders'


class OrderItemsManager(models.Manager):
    """ 注文アイテム操作
    """
    def insert_cart_items(self, cart, order):
        for item in cart.cartitems_set.all():
            self.create(
                quantity=item.quantity,
                product=item.product,
                order=order
            )


class OrderItems(models.Model):
    """ 注文アイテムテーブル
    """
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    objects = OrderItemsManager()

    class Meta:
        db_table = 'order_items'
        unique_together = [['product', 'order']]
