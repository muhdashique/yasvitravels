from django.urls import path
from . import views  # Ensure this import works correctly

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('property/',views.property,name='property'),
    path('service/',views.service,name='service'),
    path('traveland tour/',views.travelandtour,name='travelandtour'),
    path('login/', views.login_view, name='login'),
    path('adminpannel/', views.adminpannel, name='adminpannel'),
    path('logout/', views.logout_view, name='logout'),
    path('add-destination/', views.add_destination, name='add_destination'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-segment/', views.add_segment, name='add_segment'),
    path('add-image/', views.add_image, name='add_image'),
    path('propertyview/<int:destination_id>/', views.propertyview, name='propertyview'),
    path('propertyview/<int:destination_id>/<int:category_id>/', views.propertyview, name='propertyview'),
    path('propertyview/<int:destination_id>/<int:category_id>/', views.propertyview, name='propertyview'),
    path('category/<int:category_id>/segments/', views.view_segments, name='view_segments'),
    path('segment/<int:segment_id>/images/', views.view_segment_images, name='view_segment_images'),
     path('destinations/', views.view_destinations, name='view_destinations'),
    path('destination/edit/<int:destination_id>/', views.edit_destination, name='edit_destination'),
    path('destination/delete/<int:destination_id>/', views.delete_destination, name='delete_destination'),
     path('categories/', views.manage_categories, name='manage_categories'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('segments/', views.segment_list, name='segment_list'),
    path('edit_segment/<int:pk>/', views.edit_segment, name='edit_segment'),
    path('delete_segment/<int:pk>/', views.delete_segment, name='delete_segment'),
     path('images/', views.manage_images, name='manage_images'),
    path('images/edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
   path('edit-testimonial/<int:id>/', views.edit_testimonial, name='edit_testimonial'),
      path('delete-testimonial/<int:id>/', views.delete_testimonial, name='delete_testimonial'),
     path('add-testimonial/', views.add_testimonial, name='add_testimonial'),
      path('gallery/', views.gallery_view, name='gallery'),
    path('add-gallery-image/', views.add_gallery_image, name='add_gallery_image'),
   path('delete-gallery-image/<int:id>/', views.delete_gallery_image, name='delete_gallery_image'),
    path('edit-gallery-image/<int:id>/', views.edit_gallery_image, name='edit_gallery_image'),
     path('view_packages/', views.view_packages, name='view_packages'),
    path('package_add/', views.package_add, name='package_add'),
      path('delete/<int:id>/', views.delete_package, name='delete_package'),
      path('edit/<int:id>/', views.edit_package, name='edit_package'),

     
    path('add-campingimage/', views.add_campingimage, name='add_campingimage'),
    path('edit-campingimage/<int:image_id>/', views.edit_campingimage, name='edit_campingimage'),
     path('edit_campingimage/<int:image_id>/', views.edit_campingimage, name='edit_campingimage'),
    path('delete_campingimage/<int:image_id>/', views.delete_campingimage, name='delete_campingimage'),
      path('add_segment/', views.add_segment, name='add_segment'),
    path('get_categories/', views.get_categories, name='get_categories'),
     path('get_segments/', views.get_segments, name='get_segments'),
    path('send-email/', views.send_email, name='send_email'),
]

    

      



  


   
   
  
      


    
 
    





