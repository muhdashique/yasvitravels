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






]