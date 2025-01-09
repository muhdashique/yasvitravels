from django.db import models


# models.py

class Destination(models.Model):
    name = models.CharField(max_length=100)
    destination_image = models.ImageField(upload_to='destinations/', null=True, blank=True) 

    def __str__(self):
        return self.name


class Category(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='categories/', null=True, blank=True) 

    def __str__(self):
        return self.name


class Segment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)  # Description field
    segment_image = models.ImageField(upload_to='segments/', null=True, blank=True)  # Image field

    def __str__(self):
        return self.name



class Image(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title or "Image"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    review = models.TextField()

    def __str__(self):
        return self.name
    



from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category
class Package(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to='package_images/')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True, choices=[(True, 'Available'), (False, 'Not Available')])

    def __str__(self):
        return self.name






class CampingImage(models.Model):
    image = models.ImageField(upload_to='camping_images/')
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)  # New field for name
    details = models.TextField(blank=True, null=True)  # New field for details
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # New field for amount
    status = models.BooleanField(default=True, choices=[(True, 'Available'), (False, 'Not Available')])

    def __str__(self):
        return f"{self.name} - {'Available' if self.status else 'Not Available'}"


