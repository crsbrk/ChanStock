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
    
    timer='1'

    if request.method == "POST":
        timer = request.POST.get('timer')
    
    print("timer is %s",timer)
    stock_type = stock.stock_type
    stock_k_one_data = getStockOneMinute(id, timer, stock_type)
    stock_zs_data = getStockZs(id,timer,stock_type)
    stock_buysell_data = getStockBuySell(id,timer,stock_type)

    json_data=json.dumps(stock_k_one_data,ensure_ascii=False)
    json_zs_data=json.dumps(stock_zs_data,ensure_ascii=False)
    json_buysell_data=json.dumps(stock_buysell_data,ensure_ascii=False)    
    print(json_buysell_data)




    context = {
        'stock': stock,
        'stock_k_one_json': json_data,
        'stock_zs_json':stock_zs_data,
        'stock_buysell_json':stock_buysell_data,
        'timer':timer

    }

    return render(request, 'stocks/details.html', context)


def about(request):
    return HttpResponse("缠论")


def getStockOneMinute(stock_id,timer, stock_type):
    table_name ='1'
    if timer == 'one':
        table_name = '1'
    if timer == 'thirty':
        table_name = '30'
    if timer == 'day':
        table_name = 'd'
    if timer == 'month':
        table_name = 'm'
    if timer == 'week':
        table_name = 'w'
    if timer == 'five':
        table_name = '5'

    stock_table_name ='kbars_'+table_name+'_'+stock_id+'_'+stock_type     
    sql1 ='SELECT * FROM '+stock_table_name+'  ORDER BY id DESC LIMIT 1000'
    sql ='SELECT * FROM ('+sql1+')sub ORDER BY id ASC;'

    symbol_name = stock_id+'.'+stock_type.upper()
    resol_name = table_name.upper()
    print(resol_name)
    print(resol_name)

    sql_zs = '''selecct fromts, tots, zd, zg from tbzs where symbol= '%s' and resol='%s' ORDER BY id DESC LIMIT 1000'''%(symbol_name,resol_name)
    print(sql)
    print(sql_zs)

    db = pymysql.connect('localhost','django','django@1','chan_stock')
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

def getStockZs(stock_id,timer, stock_type):
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

    stock_table_name ='kbars_'+table_name+'_'+stock_id+'_'+stock_type     


    symbol_name = stock_id+'.'+stock_type.upper()
    resol_name = table_name.upper()
    print(symbol_name)
    print(resol_name)

    sql_zs = '''SELECT fromts, tots, zd, zg from tbzs where symbol= '%s' and resol='%s' ORDER BY fromts DESC LIMIT 1000'''%(symbol_name,resol_name)
    

    sql ='SELECT * FROM ('+sql_zs+')sub ORDER BY fromts ASC;'
    print(sql)
    db = pymysql.connect('localhost','django','django@1','chan_stock')
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

        
def getStockBuySell(stock_id,timer, stock_type):
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

    stock_table_name = 'buysell' 


    symbol_name = stock_id+'.'+stock_type.upper()
    resol_name = table_name.upper()
    print(symbol_name)
    print(resol_name)

    sql_buysell = '''SELECT pdate, price, ptype  from buysell where symbol= '%s' and resol='%s' ORDER BY fromts DESC LIMIT 10'''%(symbol_name,resol_name)
    

    sql ='SELECT * FROM ('+sql_buysell+')sub ORDER BY pdate ASC;'
    print(sql)
    db = pymysql.connect('localhost','django','django@1','chan_stock')
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