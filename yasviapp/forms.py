# forms.py

from django import forms
from .models import CampingImage, Destination, Category, GalleryImage, Package, Segment, Image, Testimonial

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


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'review']


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'category', 'description']



class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'details', 'image', 'amount', 'status']




class CampingImageForm(forms.ModelForm):
    class Meta:
        model = CampingImage
        fields = ['image', 'description', 'name', 'details', 'amount', 'status']
