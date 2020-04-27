from django.shortcuts import render
from django.http import HttpResponse
from .models import Stocks
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import pymysql,json

def index(request):
  
    stocks = Stocks.objects.all()
    paginator = Paginator(stocks, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {
         'title':'缠论',
         'stocks':listings

    }

    return render(request, 'stocks/index.html', context)

def details(request, id):
    stock = Stocks.objects.get(stock_id=id)
    
    stock_k_one_data = getStockOneMinute(id)
    json_data=json.dumps(stock_k_one_data,ensure_ascii=False)
    print(json_data)




    context = {
        'stock': stock,
        'stock_k_one_json': json_data
    }

    return render(request, 'stocks/details.html', context)


def about(request):
    return HttpResponse("缠论")


def getStockOneMinute(stock_id):
    sql ='SELECT * FROM kbars_1_'+stock_id+'  LIMIT 0,100;'
    print(sql)
    db = pymysql.connect('localhost','root','root','chan_stock')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    list_all = []

    for row in data:
        list_one = []
        for r in row:
            list_one.append(r)
        list_all.append(list_one)

    db.close()

    return list_all