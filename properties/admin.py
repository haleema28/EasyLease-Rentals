from django.contrib import admin
from .models import Property, PropertyImage, Amenity, Wishlist, Booking

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class AmenityInline(admin.TabularInline):
    model = Property.amenities.through
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'listing_type', 'price', 'location', 'is_available')
    list_filter = ('property_type', 'listing_type', 'is_available')
    search_fields = ('title', 'location', 'address')
    inlines = [PropertyImageInline, AmenityInline]
    exclude = ('amenities',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'property__title')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'move_in_date', 'duration_months', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'property__title')
    readonly_fields = ('booking_date',)
