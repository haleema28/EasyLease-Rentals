from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from properties.models import Property, PropertyImage, Amenity
from decimal import Decimal
from django.core.files import File
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Adds sample properties to the database'

    def handle(self, *args, **kwargs):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

        # Create amenities
        amenities = [
            'Parking',
            'Swimming Pool',
            'Gym',
            'Security',
            'Power Backup',
            'Lift',
            'Garden',
            'Play Area',
            '24/7 Water Supply',
            'Internet'
        ]

        for amenity_name in amenities:
            Amenity.objects.get_or_create(name=amenity_name)

        # Create default image if it doesn't exist
        default_image_path = 'media/property_images/default.jpg'
        if not os.path.exists(default_image_path):
            # Create a simple colored image
            img = Image.new('RGB', (800, 600), color='#f0f0f0')
            img.save(default_image_path)

        # Property data
        property_data = [
            # 1BHK Properties
            {
                'title': 'Cozy 1BHK Apartment',
                'property_type': '1BHK',
                'listing_type': 'RENTAL',
                'price': Decimal('15000'),
                'security_deposit': Decimal('30000'),
                'area': 500,
                'location': 'Downtown',
                'address': '123 Main Street, Downtown',
                'description': 'Beautiful 1BHK apartment in the heart of the city.',
                'amenities': ['Parking', 'Security', 'Lift']
            },
            {
                'title': 'Modern 1BHK Flat',
                'property_type': '1BHK',
                'listing_type': 'LEASE',
                'price': Decimal('12000'),
                'security_deposit': Decimal('24000'),
                'area': 450,
                'location': 'Suburb',
                'address': '456 Park Avenue, Suburb',
                'description': 'Modern 1BHK flat with all amenities.',
                'amenities': ['Parking', 'Security', 'Lift']
            },
            # Add more 1BHK properties...

            # 2BHK Properties
            {
                'title': 'Spacious 2BHK Apartment',
                'property_type': '2BHK',
                'listing_type': 'RENTAL',
                'price': Decimal('25000'),
                'security_deposit': Decimal('50000'),
                'area': 800,
                'location': 'City Center',
                'address': '789 High Street, City Center',
                'description': 'Spacious 2BHK apartment with modern amenities.',
                'amenities': ['Parking', 'Garden', 'Play Area', '24/7 Water Supply']
            },
            {
                'title': 'Luxury 2BHK Flat',
                'property_type': '2BHK',
                'listing_type': 'LEASE',
                'price': Decimal('22000'),
                'security_deposit': Decimal('44000'),
                'area': 750,
                'location': 'Uptown',
                'address': '321 Lake View, Uptown',
                'description': 'Luxury 2BHK flat with lake view.',
                'amenities': ['Parking', 'Security', 'Lift']
            },
            # Add more 2BHK properties...

            # 3BHK Properties
            {
                'title': 'Premium 3BHK Villa',
                'property_type': '3BHK',
                'listing_type': 'RENTAL',
                'price': Decimal('35000'),
                'security_deposit': Decimal('70000'),
                'area': 1200,
                'location': 'Luxury Hills',
                'address': '555 Luxury Lane, Luxury Hills',
                'description': 'Premium 3BHK villa with garden and pool.',
                'amenities': ['Parking', 'Swimming Pool', 'Gym', 'Security', 'Power Backup']
            },
            {
                'title': 'Modern 3BHK Apartment',
                'property_type': '3BHK',
                'listing_type': 'LEASE',
                'price': Decimal('30000'),
                'security_deposit': Decimal('60000'),
                'area': 1100,
                'location': 'Business District',
                'address': '888 Business Park, Business District',
                'description': 'Modern 3BHK apartment in business district.',
                'amenities': ['Parking', 'Security', 'Lift']
            },
            # Add more 3BHK properties...
        ]

        # Create properties
        for data in property_data:
            property_obj, created = Property.objects.get_or_create(
                title=data['title'],
                defaults={
                    'property_type': data['property_type'],
                    'listing_type': data['listing_type'],
                    'price': data['price'],
                    'security_deposit': data['security_deposit'],
                    'area': data['area'],
                    'location': data['location'],
                    'address': data['address'],
                    'description': data['description']
                }
            )
            
            if created:
                # Add amenities
                for amenity_name in data['amenities']:
                    amenity = Amenity.objects.get(name=amenity_name)
                    property_obj.amenities.add(amenity)
                
                # Create a placeholder image
                with open(default_image_path, 'rb') as f:
                    property_obj.image.save('default.jpg', File(f), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully added sample properties')) 