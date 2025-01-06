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
