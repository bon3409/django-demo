from django.db import models

# Create your models here.

class Stock(models.Model):
    class Meta:
        # 指定 table 名稱
        db_table = '"stock_lists"'

    # 定義欄位
    name = models.CharField('股票名稱', max_length=50)
    code = models.CharField('股票代號', max_length=10, blank=True)
    remark = models.CharField('備註', max_length=50)
    created_at = models.DateTimeField('建立時間', auto_now=True)

    def get_all():
        try:
            records = Stock.objects.all()
            return records;
        except Exception as e:
            print(e)
            return []

    def first_or_create(**params):
        try:
            record = Stock.objects.filter(name=params['name'], code=params['code'])[0]
        except IndexError:
            record = Stock.objects.create(name=params['name'], code=params['code'])

        return record