import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import yfinance as yf
import matplotlib
import matplotlib.pyplot as plt
import io, base64, urllib

from stock.models import Stock

# 解決出圖的問題
matplotlib.use('Agg')

class Stocks:
    def index(request):
        return render(request, 'index.html')

    @csrf_exempt
    def get_stock(request):
        try:
            if request.method == 'POST':
                type = request.POST['type']
                code = request.POST['code']
                stock = yf.Ticker(f'{code}.{type}')
                stock_name = stock.info['shortName']
                history = stock.history(period="1mo")

                # create db data
                record = Stock.first_or_create(name=stock_name, code=code)

                # 製作圖表
                date = history.index
                plt.figure(dpi=90, figsize=(12,10))
                plt.plot(date, history['Close'])
                plt.xticks(rotation=45) # rotate x axis label
                plt.xlabel('Date')
                plt.ylabel('Price')
                plt.title(f'{code} Price')

                # 如果要顯示圖表，可以用 base64 的方式回傳，並且顯示在前端畫面
                fig = plt.gcf()
                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                buf.seek(0)
                base64_string = base64.b64encode(buf.read())
                uri = urllib.parse.quote(base64_string)

                return JsonResponse({'status': True, 'image': uri})
            else:
                raise Exception('method error')
        except Exception as e:
            print(e)

        return JsonResponse({'status': False})

    def search_history(request):
        records = Stock.get_all()
        return render(request, 'search-history.html', {'records': records})