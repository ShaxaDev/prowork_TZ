from account.models import Territory
from blog.models import Category
from django import forms

class FilterForm(forms.Form):
    categories=forms.ModelChoiceField(label='Kategoriya',empty_label='Kategoriya tanlang',queryset=Category.objects.all(),required=False)
    territories=forms.ModelChoiceField(label='Xudud',empty_label='Xudud tanlang',queryset=Territory.objects.all(),required=False)