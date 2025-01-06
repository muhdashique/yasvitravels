from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Destination, Category, Segment, Image
from .forms import DestinationForm, CategoryForm, SegmentForm, ImageForm

from django.contrib.auth.forms import AuthenticationForm

# Public Views
def index(request):
    destinations = Destination.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {'destinations': destinations, 'categories': categories})

def about(request):
    return render(request, 'about.html')

def property(request):
    destination_id = request.GET.get('destination_id')  # Get the destination ID from the query parameter
    destinations = Destination.objects.all()
    
    if destination_id:
        categories = Category.objects.filter(destination_id=destination_id)  # Filter by destination ID
    else:
        categories = Category.objects.all()
    
    return render(request, "property.html", {
        'destinations': destinations,
        # 'categories': categories,
    })


def travelandtour(request):
    return render(request, "travelandtour.html")

def gallery(request):
    images = Image.objects.all()
    return render(request, "gallery.html", {'images': images})

def blog(request):
    return render(request, "blog.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    return render(request, "contact.html")

# Authentication Views
# views.py



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminpannel')  # Redirect to admin panel after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('index')

# Admin Views - Protected with login_required
@login_required(login_url='login')
def adminpannel(request):
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
        'destination_form': DestinationForm(),
        'category_form': CategoryForm(),
        'segment_form': SegmentForm(),
        'image_form': ImageForm(),
    }
    return render(request, 'adminpannel.html', context)

@login_required(login_url='login')
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)  # Use request.FILES to handle image upload
        if form.is_valid():
            form.save()  # Save the destination along with the image
            return redirect('adminpannel')  # Redirect to the index page or any page you want after adding
    else:
        form = DestinationForm()
    return render(request, 'adminpannel.html', {'destination_form': form})



@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpannel')  # Redirect to the index or another page
    else:
        form = CategoryForm()
    return render(request, 'adminpannel.html', {'category_form': form})



@login_required(login_url='login')
def add_segment(request):
    if request.method == "POST":
        form = SegmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Segment added successfully!')
            return redirect('adminpannel')
        messages.error(request, 'Please correct the errors below.')
    return redirect('adminpannel')

@login_required(login_url='login')
def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added successfully!')
            return redirect('adminpannel')
        messages.error(request, 'Please correct the errors below.')
    return redirect('adminpannel')


def propertyview(request, destination_id):
    # Get the selected destination
    destination = Destination.objects.get(id=destination_id)

    # Filter categories under this destination
    categories = Category.objects.filter(destination=destination)

    return render(request, "property_view.html", {
        # 'destination': destination,
        'categories': categories,
    })
