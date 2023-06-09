from django import forms

class StockPredictionForm(forms.Form):
    stock_name = forms.CharField(label='종목명', max_length=100)
    page_size = forms.IntegerField(label='페이지 사이즈')
