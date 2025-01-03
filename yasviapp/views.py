from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# home page views
def index(request):
    return render(request,"index.html")

# about page views
def about(request):
    return render(request, 'about.html')


# property page views
def property(request):
    return render(request,"property.html")

# travel and tour page view
def travelandtour(request):
    return render(request,"travelandtour.html")

# gallery page view
def gallery(request):
    return render(request,"gallery.html")

# blog page view
def blog(request):
    return render(request,"blog.html")

# sevice page view
def service(request):
    return render(request,"service.html")

# contact page view
def contact(request):
    return render(request,"contact.html")