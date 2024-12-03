from django import forms
from .models import Item

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_image']