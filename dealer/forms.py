from django import forms
from .models import Items


class AddItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = "__all__"
