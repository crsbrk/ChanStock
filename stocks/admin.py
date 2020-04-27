from django.contrib import admin
from .models import Stocks
# Register your models here.

from .models import Stocks

class StocksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stocks._meta.get_fields()]
    list_per_page = 25


admin.site.register(Stocks, StocksAdmin)
