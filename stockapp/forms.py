from django import forms

class StockPredictionForm(forms.Form):
    market = forms.CharField(label='market', max_length=10)
    pageSize = forms.IntegerField(label='pageSize')
