from django import forms



class testForm(forms.Form):
    test = forms.CharField(max_length=30, label='test')
    
