from django import forms

class StockPredictionForm(forms.Form):
    market = forms.CharField(label='market')

class StockPredictionForm(forms.Form):
    market = forms.CharField(label='market')
    pageSize = forms.IntegerField(label='pageSize')
    page = forms.IntegerField(label='page')