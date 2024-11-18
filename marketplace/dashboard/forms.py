from django import forms
from item.models import Item


class EditItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image", "is_sold")
