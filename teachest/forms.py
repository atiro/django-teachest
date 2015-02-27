from django import forms
from django.forms.extras.widgets import Select

class TeaForm(forms.Form):
    maker = forms.CharField(max_length=20,widget=Select(choices=(('richard', 'Richard'), ('james', 'James'))))

    quantity = forms.IntegerField(widget=Select(choices=[(i,i,) for i in range(1,10)]))
    type = forms.CharField(max_length=20)
    sprint = forms.IntegerField(widget=Select(choices=[(i,i,) for i in range(1,25)]))

