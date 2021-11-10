from django.db import models


class Product(models.Model):
    '''Model product. Add product in Admin panel'''
    name = models.CharField(max_length=200, verbose_name='Name of product')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    created = models.DateTimeField(auto_now_add=True)

    def get_name(self):
        return self.name + ' it`s a cool.'

    class Meta:
        ordering = ('name',)
        index_together = ('id',)

    def __str__(self):
        return self.name


class Order(models.Model):
    '''Order we created from Product model.'''
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, db_index=True)

    class Meta:
        ordering = ['created']


class Score(models.Model):
    order = models.ForeignKey(Order, related_name='score_order', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']





