# forms.py

from django import forms
from .models import Destination, Category, Segment, Image

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'destination_image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['destination', 'name', 'category_image']

class SegmentForm(forms.ModelForm):
    class Meta:
        model = Segment
        fields = ['destination', 'category', 'name', 'description', 'segment_image']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['destination', 'category', 'segment', 'image', 'title']
