from django.shortcuts import render
from django.http import HttpResponse
from .models import Stocks
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import pymysql,json

from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
def details(request, id):
    stock = Stocks.objects.get(stock_id=id)
    
    timer='D'
    if request.method == "POST":
        timer = request.POST.get('timer')
    
    print("timer is %s",timer)

    stock_k_one_data = getStockOneMinute(id, timer)
    json_data=json.dumps(stock_k_one_data,ensure_ascii=False)
    #print(json_data)




    context = {
        'stock': stock,
        'stock_k_one_json': json_data,
        'timer':timer

    }

    return render(request, 'stocks/details.html', context)


def about(request):
    return HttpResponse("缠论")


def getStockOneMinute(stock_id,timer):
    table_name ='1'
    if timer == 'one':
        table_name = '1'
    if timer == 'thirty':
        table_name = '30'
    if timer == 'day':
        table_name = 'D'
    if timer == 'month':
        table_name = 'M'
    if timer == 'week':
        table_name = 'W'
    if timer == 'five':
        table_name = '5'

    sql ='SELECT * FROM kbars_'+table_name+'_'+stock_id+'  ;'
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