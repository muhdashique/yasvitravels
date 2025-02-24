from django.urls import path
from . import views  # Ensure this import works correctly

urlpatterns = [
    path('', views.index, name='index'), #index page index.html
    path('about/', views.about, name='about'),#about page  about.html
    path('contact/',views.contact,name='contact'),#  contact page     contact.html
    path('gallery/',views.gallery,name='gallery'),#  gallery page     gallery.html
    path('property/',views.property,name='property'),# property page     property.html
    path('service/',views.service,name='service'),#  service page     service.html
    path('traveland tour/',views.travelandtour,name='travelandtour'),#  travel and tour page     traveland tour.html
    path('login/', views.login_view, name='login'),#  login page     login.html
    path('adminpannel/', views.adminpannel, name='adminpannel'),#  admin pannel page     adminpannel.html
    path('logout/', views.logout_view, name='logout'),#  logoutpage     adminpnnel.html
    path('add-destination/', views.add_destination, name='add_destination'),#  destination adding page    add_destination.html
    path('add-category/', views.add_category, name='add_category'),#  category adding page     .html
    path('add-segment/', views.add_segment, name='add_segment'),#  page     .html
    path('add-image/', views.add_image, name='add_image'),#  page     .html
    path('propertyview/<int:destination_id>/', views.propertyview, name='propertyview'),#  page     .html
    path('propertyview/<int:destination_id>/<int:category_id>/', views.propertyview, name='propertyview'),#  page     .html
    path('propertyview/<int:destination_id>/<int:category_id>/', views.propertyview, name='propertyview'),#  page     .html
    path('category/<int:category_id>/segments/', views.view_segments, name='view_segments'),#  page     .html
    path('segment/<int:segment_id>/images/', views.view_segment_images, name='view_segment_images'),#  page     .html
    path('destinations/', views.view_destinations, name='view_destinations'),#  page     .html
    path('destination/edit/<int:destination_id>/', views.edit_destination, name='edit_destination'),#  page     .html
    path('destination/delete/<int:destination_id>/', views.delete_destination, name='delete_destination'),#  page     .html
    path('categories/', views.manage_categories, name='manage_categories'),#  page     .html
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),#  page     .html
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),#  page     .html
    path('segments/', views.segment_list, name='segment_list'),#  page     .html
    path('edit_segment/<int:pk>/', views.edit_segment, name='edit_segment'),#  page     .html
    path('delete_segment/<int:pk>/', views.delete_segment, name='delete_segment'),#  page     .html
    path('images/', views.manage_images, name='manage_images'),#  page     .html
    path('images/edit/<int:image_id>/', views.edit_image, name='edit_image'),#  page     .html
    path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),#  page     .html
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),#  page     .html
    path('edit-testimonial/<int:id>/', views.edit_testimonial, name='edit_testimonial'),#  page     .html
    path('delete-testimonial/<int:id>/', views.delete_testimonial, name='delete_testimonial'),#  page     .html
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),#  page     .html
    path('gallery/', views.gallery_view, name='gallery'),#  page     .html
    path('add-gallery-image/', views.add_gallery_image, name='add_gallery_image'),#  page     .html
    path('delete-gallery-image/<int:id>/', views.delete_gallery_image, name='delete_gallery_image'),#  page     .html
    path('edit-gallery-image/<int:id>/', views.edit_gallery_image, name='edit_gallery_image'),#  page     .html
    path('view_packages/', views.view_packages, name='view_packages'),#  page     .html
    path('package_add/', views.package_add, name='package_add'),#  page     .html
    path('delete/<int:id>/', views.delete_package, name='delete_package'),#  page     .html
    path('edit/<int:id>/', views.edit_package, name='edit_package'),#  page     .html
    path('add-campingimage/', views.add_campingimage, name='add_campingimage'),#  page     .html
    path('edit-campingimage/<int:image_id>/', views.edit_campingimage, name='edit_campingimage'),#  page     .html
    path('edit_campingimage/<int:image_id>/', views.edit_campingimage, name='edit_campingimage'),#  page     .html
    path('delete_campingimage/<int:image_id>/', views.delete_campingimage, name='delete_campingimage'),#  page     .html
    path('add_segment/', views.add_segment, name='add_segment'),#  page     .html
    path('get_categories/', views.get_categories, name='get_categories'),#  page     .html
    path('get_segments/', views.get_segments, name='get_segments'),#  page     .html
    path('send-email/', views.send_email, name='send_email'),#  page     .html
    path('tourpackage/', views.tourpackage, name='tourpackage'),#  page     .html
]

    

      



  


   
   
  
      


    
 
    





