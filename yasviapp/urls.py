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
    
 
    






]