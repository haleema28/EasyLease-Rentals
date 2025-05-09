from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('1BHK', '1 BHK'),
        ('2BHK', '2 BHK'),
        ('3BHK', '3 BHK'),
    ]
    
    LISTING_TYPES = [
        ('RENTAL', 'Rental'),
        ('LEASE', 'Lease'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.IntegerField(help_text='Area in square feet')
    location = models.CharField(max_length=200)
    address = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_properties')
    
    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.property.title}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    properties = models.ManyToManyField(Property, related_name='amenities')

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')
    
    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.property.title}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    duration_months = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    security_deposit_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s booking - {self.property.title}"
