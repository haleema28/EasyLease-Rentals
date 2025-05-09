from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Property, PropertyImage, Wishlist, Booking
from .forms import PropertySearchForm, BookingForm

def home(request):
    featured_properties = Property.objects.filter(is_available=True).order_by('-created_at')[:6]
    return render(request, 'properties/home.html', {
        'featured_properties': featured_properties
    })

def property_list(request):
    properties = Property.objects.filter(is_available=True)
    search_form = PropertySearchForm(request.GET)
    
    if search_form.is_valid():
        property_type = search_form.cleaned_data.get('property_type')
        listing_type = search_form.cleaned_data.get('listing_type')
        min_price = search_form.cleaned_data.get('min_price')
        max_price = search_form.cleaned_data.get('max_price')
        
        if property_type:
            properties = properties.filter(property_type=property_type)
        if listing_type:
            properties = properties.filter(listing_type=listing_type)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)
    
    return render(request, 'properties/property_list.html', {
        'properties': properties,
        'search_form': search_form
    })

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    images = property.images.all()
    amenities = property.amenities.all()
    is_in_wishlist = False
    
    if request.user.is_authenticated:
        is_in_wishlist = Wishlist.objects.filter(user=request.user, property=property).exists()
    
    return render(request, 'properties/property_detail.html', {
        'property': property,
        'images': images,
        'amenities': amenities,
        'is_in_wishlist': is_in_wishlist
    })

@login_required
def book_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.property = property
            booking.save()
            return redirect('payment_success', booking_id=booking.id)
    else:
        form = BookingForm()
    
    return render(request, 'properties/book_property.html', {
        'property': property,
        'form': form
    })

@login_required
def add_to_wishlist(request, pk):
    property = get_object_or_404(Property, pk=pk)
    Wishlist.objects.get_or_create(user=request.user, property=property)
    messages.success(request, 'Property added to wishlist!')
    return redirect('property_detail', pk=pk)

@login_required
def remove_from_wishlist(request, pk):
    property = get_object_or_404(Property, pk=pk)
    Wishlist.objects.filter(user=request.user, property=property).delete()
    messages.success(request, 'Property removed from wishlist!')
    return redirect('property_detail', pk=pk)

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'properties/wishlist.html', {
        'wishlist_items': wishlist_items
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'properties/my_bookings.html', {
        'bookings': bookings
    })

@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = 'CONFIRMED'
    booking.security_deposit_paid = True
    booking.save()
    
    return render(request, 'properties/payment.html', {
        'booking': booking
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
