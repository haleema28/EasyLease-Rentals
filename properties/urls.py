from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:pk>/book/', views.book_property, name='book_property'),
    path('property/<int:pk>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('property/<int:pk>/remove-from-wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('register/', views.register, name='register'),
] 