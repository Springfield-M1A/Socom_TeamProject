from django import forms

class StockPredictionForm(forms.Form):
    market = forms.CharField(label='market')
    code = forms.CharField(label='code')
    normalization = forms.CharField(label='normalization')