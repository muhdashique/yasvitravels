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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial querysets
        self.fields['category'].queryset = Category.objects.none()
        
        if 'instance' in kwargs and kwargs['instance']:
            destination = kwargs['instance'].destination
            if destination:
                self.fields['category'].queryset = Category.objects.filter(destination=destination)
                
        # If we have POST data
        elif args and args[0]:
            destination_id = args[0].get('destination')
            if destination_id:
                self.fields['category'].queryset = Category.objects.filter(destination_id=destination_id)

    def clean(self):
        cleaned_data = super().clean()
        destination = cleaned_data.get('destination')
        category = cleaned_data.get('category')
        
        if category and destination and category.destination != destination:
            raise forms.ValidationError("Selected category does not belong to the selected destination.")
        
        return cleaned_data

# forms.py
from django import forms
from .models import Image, Category, Segment

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['destination', 'category', 'segment', 'image', 'title']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial querysets
        self.fields['category'].queryset = Category.objects.none()
        self.fields['segment'].queryset = Segment.objects.none()
        
        # If we have an instance or initial destination, populate the categories
        instance = kwargs.get('instance')
        if instance:
            self.fields['category'].queryset = Category.objects.filter(
                destination=instance.destination
            )
            self.fields['segment'].queryset = Segment.objects.filter(
                category=instance.category
            )
        
        # If we have POST data
        elif args and args[0]:
            destination_id = args[0].get('destination')
            category_id = args[0].get('category')
            if destination_id:
                self.fields['category'].queryset = Category.objects.filter(
                    destination_id=destination_id
                )
            if category_id:
                self.fields['segment'].queryset = Segment.objects.filter(
                    category_id=category_id
                )

    def clean(self):
        cleaned_data = super().clean()
        destination = cleaned_data.get('destination')
        category = cleaned_data.get('category')
        segment = cleaned_data.get('segment')

        if category and category.destination != destination:
            raise forms.ValidationError(
                "Selected category does not belong to the selected destination."
            )
        
        if segment and segment.category != category:
            raise forms.ValidationError(
                "Selected segment does not belong to the selected category."
            )
        
        return cleaned_data


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



from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
