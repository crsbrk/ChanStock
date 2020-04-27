from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
#from templates.constant_files import WORKERS_NAMES, ORDER_TYPES

# Create your models here.


class Stocks(models.Model):

    #title is project name
    stock_name = models.CharField('名称代码', max_length=200)
    stock_id = models.CharField("股票id", max_length=200)
    stock_price = models.FloatField('价格', default=0)
    stock_change = models.FloatField('涨跌幅', default=0)
    stock_market_value = models.FloatField('市值', default=0)

    def __str__(self):
        return self.stock_name

    class Meta:
        verbose_name_plural = "stocks"
        verbose_name = "stock lists"