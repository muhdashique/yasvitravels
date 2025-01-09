from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CampingImage, Destination, Category, GalleryImage, Segment, Image, Testimonial
from .forms import CampingImageForm, DestinationForm, CategoryForm, GalleryImageForm, SegmentForm, ImageForm, TestimonialForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Segment
from django.shortcuts import render, get_object_or_404
from .models import Segment, Image
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect




# Public Views
def index(request):
    destinations = Destination.objects.all()[:6]
    categories = Category.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    gallery_images = GalleryImage.objects.all()
    packages = Package.objects.all()
    images = CampingImage.objects.all()
    return render(request, "index.html", {'destinations': destinations, 'categories': categories,'testimonials': testimonials,'gallery_images': gallery_images,'packages': packages,'images': images})

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
    packages = Package.objects.all()
    images = CampingImage.objects.all()
    return render(request, "travelandtour.html", {'packages': packages,'images': images})

def gallery(request):
    images = Image.objects.all()
    gallery_images = GalleryImage.objects.all()
    return render(request, "gallery.html", {'images': images,'gallery_images': gallery_images})
 

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
        # 'destination_form': DestinationForm(),
        'category_form': CategoryForm(),
        'segment_form': SegmentForm(),
        'image_form': ImageForm(),
    }
    return render(request, 'adminpannel.html', context)

@login_required(login_url='login')

def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_destination')  # Reload the page to show the updated list
    else:
        form = DestinationForm()
    
    destinations = Destination.objects.all()  # Fetch all destinations
    return render(request, 'destinations.html', {'destination_form': form, 'destinations': destinations})




@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')  # Redirect to the index or another page
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'category_form': form})



@login_required(login_url='login')
def add_segment(request):
    if request.method == 'POST':
        form = SegmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('segment_list')  # Redirect to a page listing all segments
    else:
        form = SegmentForm()
    return render(request, 'segment.html', {'segment_form': form})


@login_required(login_url='login')
def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added successfully!')
            return redirect('view_segment_images')
        messages.error(request, 'Please correct the errors below.')
    return redirect('view_segment_imagesl')


def propertyview(request, destination_id):
    # Get the selected destination
    destination = Destination.objects.get(id=destination_id)

    # Filter categories under this destination
    categories = Category.objects.filter(destination=destination)

    return render(request, "property_view.html", {
        # 'destination': destination,
        'categories': categories,
    })



# views.py


def view_segments(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    segments = Segment.objects.filter(category=category)

    return render(request, 'view_segments.html', {
        'category': category,
        'segments': segments,
    })



# views.py


def view_segment_images(request, segment_id):
    segment = get_object_or_404(Segment, id=segment_id)
    images = Image.objects.filter(segment=segment)

    return render(request, 'view_segment_images.html', {
        'segment': segment,
        'images': images,
    })




from django.shortcuts import render
from .models import Destination

def view_destinations(request):
    destinations = Destination.objects.all()  # Fetch destinations in the defined order
    return render(request, 'destinations.html', {'destinations': destinations})


from django.shortcuts import get_object_or_404, render, redirect
from .forms import DestinationForm
from .models import Destination

def edit_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('view_destinations')  # Redirect to the destinations list after editing
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'edit_destination.html', {'destination_form': form, 'destination': destination})



from django.shortcuts import get_object_or_404, redirect
from .models import Destination

def delete_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    destination.delete()
    return redirect('view_destinations')  # Redirect to the destinations list after deletion






from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def manage_categories(request):
    # Handle category form submission
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm()

    # Get all categories
    categories = Category.objects.all()

    return render(request, 'category.html', {'category_form': form, 'categories': categories})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'category_form': form, 'category': category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('manage_categories')


def segment_list(request):
    segments = Segment.objects.all()
    return render(request, 'segment.html', {'segments': segments})



def edit_segment(request, pk):
    segment = Segment.objects.get(pk=pk)
    if request.method == 'POST':
        form = SegmentForm(request.POST, request.FILES, instance=segment)
        if form.is_valid():
            form.save()
            return redirect('segment_list')
    else:
        form = SegmentForm(instance=segment)
    return render(request, 'edit_segment.html', {'segment_form': form})





def delete_segment(request, pk):
    segment = Segment.objects.get(pk=pk)
    if request.method == 'POST':
        segment.delete()
        return redirect('segment_list')
    return render(request, 'delete_segment.html', {'segment': segment})





from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm

def manage_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_images')
    else:
        form = ImageForm()
    
    images = Image.objects.all()
    return render(request, 'add_image.html', {'form': form, 'images': images})

def edit_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('manage_images')
    else:
        form = ImageForm(instance=image)
    return render(request, 'edit_image.html', {'form': form, 'image': image})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('manage_images')





# View to list testimonials
def testimonials_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'tl', {'testimonials': testimonials})

# View to add a new testimonial
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')
    else:
        form = TestimonialForm()
    
    testimonials = Testimonial.objects.all()
    return render(request, 'add_testimonial.html', {'form': form, 'testimonials': testimonials})


# View to edit an existing testimonial
def edit_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('add_testimonial')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'edit_testimonial.html', {'form': form})



from django.shortcuts import get_object_or_404, redirect
from .models import Testimonial
from django.contrib import messages  # Optional, for feedback

def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully')  # Optional
        return redirect('add_testimonial')
    return redirect('add_testimonial')

# views.py
def gallery_view(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery_imageadd.html', {'gallery_images': gallery_images})


# views.py
def add_gallery_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_gallery_image')  # Redirect to gallery page
    else:
        form = GalleryImageForm()
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery_imageadd.html', {'form': form, 'gallery_images': gallery_images})




def edit_gallery_image(request, id):
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('add_gallery_image')  # Redirect to the gallery page
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'gallery_imageedit.html', {'form': form, 'image': image})


def delete_gallery_image(request, id):
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'image deleted successfully')  # Optional
        return redirect('add_gallery_image')
    return redirect('add_gallery_image')





from django.shortcuts import render, get_object_or_404, redirect
from .models import Package
from .forms import PackageForm

def view_packages(request):
    packages = Package.objects.all()
    return render(request, 'package_form.html', {'packages': packages})


def package_add(request):
    if request.method == 'POST':
        print('POST request received')
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('package_add')
    else:
        print('GET request received')
        form = PackageForm()
        packages = Package.objects.all()
    return render(request, 'package_form.html', {'form': form,'packages': packages})


def edit_package(request, id):
    package = Package.objects.get(pk=id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('package_add')
    else:
        form = PackageForm(instance=package)
    return render(request, 'edit_package.html', {'form': form})



def delete_package(request, id):
    package = get_object_or_404(Package, id=id)
    if request.method == 'POST':
        package.delete()
        messages.success(request, 'image deleted successfully')  # Optional
        return redirect('package_add')
    return redirect('package_add')




def add_campingimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Handle the uploaded file
        description = request.POST.get('description', '')
        status = request.POST.get('status', True)  # Default to True (Available)

        # Create a new CampingImage instance
        CampingImage.objects.create(image=image, description=description, status=status)

        return redirect('add_campingimage')

    # Fetch all existing images to display on the page
    images = CampingImage.objects.all()

    return render(request, 'add_campingimage.html', {'images': images})

def edit_campingimage(request, image_id):
    image = get_object_or_404(CampingImage, id=image_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            image.image = request.FILES.get('image')
        image.description = request.POST.get('description', '')
        image.save()
        return redirect('add_campingimage')

    return render(request, 'edit_campingimage.html', {'image': image})


def delete_campingimage(request, image_id):
    image = get_object_or_404(CampingImage, id=image_id)
    image.delete()
    return redirect('add_campingimage')

