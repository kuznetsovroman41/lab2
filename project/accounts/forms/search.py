from django import forms

class UserSearchForm(forms.Form):
    query = forms.CharField(label='Поиск пользователей', max_length=150, required=False)
