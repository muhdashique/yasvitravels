from importlib.resources import Package
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from .models import Package


from .models import (
    CampingImage, Destination, Category, GalleryImage, 
    Segment, Image, Testimonial
)
from .forms import (
    CampingImageForm, ContactForm, DestinationForm, CategoryForm, 
    GalleryImageForm, PackageForm, SegmentForm, ImageForm, TestimonialForm
)
from django.contrib.auth.forms import AuthenticationForm




# index View page
def index(request):
    destinations = Destination.objects.all()[:8]
    categories = Category.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    gallery_images = GalleryImage.objects.all()[:6]
    packages = Package.objects.all()[:6]
    images = CampingImage.objects.all()[:6]
    return render(request, "index.html", {'destinations': destinations, 'categories': categories,'testimonials': testimonials,'gallery_images': gallery_images,'packages': packages,'images': images})


# about page view
def about(request):
    return render(request, 'about.html')



def tourpackage(request):
    packages = Package.objects.all()
    return render(request,"tourpackage.html",{'packages': packages})


# property page view
def property(request):
    destination_id = request.GET.get('destination_id') 
    destinations = Destination.objects.all()
    
    if destination_id:
        categories = Category.objects.filter(destination_id=destination_id) 
    else:
        categories = Category.objects.all()
    
    return render(request, "property.html", {
        'destinations': destinations,
        'categories': categories,
    })



# travel and tour page view
def travelandtour(request):
    packages = Package.objects.all()
    images = CampingImage.objects.all()
    return render(request, "travelandtour.html", {'packages': packages,'images': images})


# gallery page view
def gallery(request):
    images = Image.objects.all()
    gallery_images = GalleryImage.objects.all()
    return render(request, "gallery.html", {'images': images,'gallery_images': gallery_images})
 

# services page view
def service(request):
    return render(request, "service.html")


# contact page view
def contact(request):
    return render(request, "contact.html")


# login page view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminpannel')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# logout view function
def logout_view(request):
    logout(request)
    return redirect('index')

# Adminpage landing page  View
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



# destination add and related page function

# add destination page view
@login_required(login_url='login')
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_destination') 
    else:
        form = DestinationForm()
    
    destinations = Destination.objects.all()  
    return render(request, 'destinations.html', {'destination_form': form, 'destinations': destinations})


# destination view page view
def view_destinations(request):
    destinations = Destination.objects.all()  
    return render(request, 'destinations.html', {'destinations': destinations})



# destination edit page
def edit_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('add_destination') 
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'edit_destination.html', {'destination_form': form, 'destination': destination})



# delete destination views

def delete_destination(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    destination.delete()
    return redirect('view_destinations')  


# category related section page view

# add category view funtion view
@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_categories') 
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'category_form': form})

# category view function
def manage_categories(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_categories')
    else:
        form = CategoryForm()

    categories = Category.objects.all()

    return render(request, 'category.html', {'category_form': form, 'categories': categories})


# edit category function view
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


# delete category function view
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('manage_categories')
    

# category get function
def get_categories(request):
    destination_id = request.GET.get('destination_id')
    if destination_id:
        categories = Category.objects.filter(destination_id=destination_id).values('id', 'name')
        return JsonResponse(list(categories), safe=False)
    return JsonResponse([], safe=False)



# segment adding and related view functions

# add segment view function
@login_required(login_url='login')
def add_segment(request):
    if request.method == 'POST':
        form = SegmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('segment_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = SegmentForm()

    segments = Segment.objects.all()
    context = {
        'segment_form': form,  
        'segments': segments
    }
    return render(request, 'segment.html', context)


# segment view function
def get_segments(request):
    category_id = request.GET.get('category_id')
    if category_id:
        segments = Segment.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse(list(segments), safe=False)
    return JsonResponse([], safe=False)


# segment view function
def view_segments(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    segments = Segment.objects.filter(category=category)

    return render(request, 'view_segments.html', {
        'category': category,
        'segments': segments,
    })




# segment list view 
def segment_list(request):
    segments = Segment.objects.all()
    return render(request, 'segment.html', {'segments': segments})

# edit segment view
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

# delete segment view
def delete_segment(request, pk):
    segment = Segment.objects.get(pk=pk)
    if request.method == 'POST':
        segment.delete()
        return redirect('segment_list')
    return render(request, 'delete_segment.html', {'segment': segment})


# add room image view function and realated views

# add room image views
@login_required(login_url='login')
def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Image added successfully!')
                return redirect('manage_images')
            except Exception as e:
                messages.error(request, f'Error saving image: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form errors:", form.errors)  
    else:
        form = ImageForm()
    
    images = Image.objects.all()
    return render(request, 'add_image.html', {
        'form': form,
        'images': images
    })


# view room image views
def view_segment_images(request, segment_id):
    segment = get_object_or_404(Segment, id=segment_id)
    images = Image.objects.filter(segment=segment)

    return render(request, 'view_segment_images.html', {
        'segment': segment,
        'images': images,
    })

# room image manage views
from django.db.models import Q

def manage_images(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    images = Image.objects.all()

    if query:
        # Filter images based on the search term
        images = images.filter(
            Q(title__icontains=query) |
            Q(destination__name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(segment__name__icontains=query)
        )

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_images')
    else:
        form = ImageForm()

    return render(request, 'add_image.html', {'form': form, 'images': images, 'query': query})


# edit room image view
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


# delete room image views
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('manage_images')



def propertyview(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    categories = Category.objects.filter(destination=destination)

    return render(request, "property_view.html", {
        'destination': destination,
        'categories': categories,
    })




#  testimonials view views
def testimonials_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'tl', {'testimonials': testimonials})

# new testimonial add views
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


# edit testimonials views
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

# delete testimonials views
def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully')  
        return redirect('add_testimonial')
    return redirect('add_testimonial')


# gallery image add function and related function

# image gallery views
def gallery_view(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery_imageadd.html', {'gallery_images': gallery_images})


# gallery image adding views
def add_gallery_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_gallery_image')  
    else:
        form = GalleryImageForm()
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallery_imageadd.html', {'form': form, 'gallery_images': gallery_images})


# edit gallery image views
def edit_gallery_image(request, id):
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('add_gallery_image') 
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'gallery_imageedit.html', {'form': form, 'image': image})

# delete gallery image views
def delete_gallery_image(request, id):
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == 'POST':
        image.delete()
        messages.success(request, 'image deleted successfully')  
        return redirect('add_gallery_image')
    return redirect('add_gallery_image')



# adding tour package and related function

# view packages views
def view_packages(request):
    packages = Package.objects.all()
    return render(request, 'package_form.html', {'packages': packages})

# adding package views
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


# edit package views
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


# delete package views
def delete_package(request, id):
    package = get_object_or_404(Package, id=id)
    if request.method == 'POST':
        package.delete()
        messages.success(request, 'image deleted successfully')  
        return redirect('package_add')
    return redirect('package_add')


# campain details adding and related functions

# adding camping image views
def add_campingimage(request):
    if request.method == 'POST':
        image = request.FILES.get('image') 
        description = request.POST.get('description', '')
        name = request.POST.get('name', '')  
        details = request.POST.get('details', '') 
        amount = request.POST.get('amount', 0)  
        status = request.POST.get('status', True)  

        
        status = True if status.lower() == 'true' else False

        
        CampingImage.objects.create(
            image=image,
            description=description,
            name=name,
            details=details,
            amount=amount,
            status=status
        )

        return redirect('add_campingimage')


    images = CampingImage.objects.all()

    return render(request, 'add_campingimage.html', {'images': images})


# edit camping image views
def edit_campingimage(request, image_id):
    image = get_object_or_404(CampingImage, id=image_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            image.image = request.FILES.get('image')
        image.description = request.POST.get('description', '')
        image.name = request.POST.get('name', '')
        image.details = request.POST.get('details', '')
        image.amount = request.POST.get('amount', 0)  
        image.status = request.POST.get('status', True)  

        
        image.status = True if image.status.lower() == 'true' else False

        image.save()
        return redirect('add_campingimage')

    return render(request, 'edit_campingimage.html', {'image': image})


# delete camping image views
def delete_campingimage(request, image_id):
    image = get_object_or_404(CampingImage, id=image_id)
    image.delete()
    return redirect('add_campingimage')


# mail sending views

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            formatted_message = (
                f"New Contact Form Submission:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {message}\n"
            )

            try:
                send_mail(
                    f"Contact Form Submission by {name}",  
                    formatted_message,                   
                    settings.EMAIL_HOST_USER,           
                    [settings.EMAIL_HOST_USER],         
                )
                return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data.'})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    




# def manage_images(request):
#     images = Image.objects.all()
    
#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         images = images.filter(title__icontains=search_term)
    
#     return render(request, 'add_image.html', {'images': images})   