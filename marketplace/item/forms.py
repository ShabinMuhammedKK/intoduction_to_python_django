from django import forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "category", "image", "is_sold")

    # name = forms.CharField(widget=(forms.TextInput(attr=({"placeholder": "Product Name"}))))
    # description = forms.CharField(widget=(forms.Textarea(attr=({"placeholder":"Description"}))))
    # price = forms.NumberInput()
    # category = forms.CharField(forms.TextInput)
    # imagage = forms
    # is_sold = forms.CheckboxInput()