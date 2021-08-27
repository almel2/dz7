from django import forms


class UserForm(forms.Form):
    kat1 = forms.IntegerField(min_value=1, label='Катет 1')
    kat2 = forms.IntegerField(min_value=1, label='Катет 2')
