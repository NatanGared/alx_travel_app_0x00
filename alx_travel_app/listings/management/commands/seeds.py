import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from models import Listing, Booking, Review
from datetime import datetime, timedelta
import uuid

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **options):
        self.stdout.write('Deleting existing data...')
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write('Creating sample users...')
        host = User.objects.create_user(
            username='travelhost',
            email='host@travelapp.com',
            password='hostpass123',
            first_name='Alex',
            last_name='Hosterson'
        )

        guest1 = User.objects.create_user(
            username='traveler1',
            email='guest1@travelapp.com',
            password='guestpass123',
            first_name='Sam',
            last_name='Traveler'
        )

        guest2 = User.objects.create_user(
            username='traveler2',
            email='guest2@travelapp.com',
            password='guestpass123',
            first_name='Jamie',
            last_name='Explorer'
        )

        self.stdout.write('Creating sample listings...')
        listings = [
            Listing.objects.create(
                host=host,
                title='Luxury Apartment in Downtown',
                description='Modern apartment with stunning city views',
                property_type='APARTMENT',
                price_per_night=150.00,
                bedrooms=2,
                bathrooms=1,
                max_guests=4,
                address='123 Main Street',
                city='New York',
                country='USA',
                amenities=['WiFi', 'Air Conditioning', 'Kitchen', 'Washer']
            ),
            Listing.objects.create(
                host=host,
                title='Cozy Mountain Cabin',
                description='Perfect getaway with mountain views',
                property_type='CABIN',
                price_per_night=95.00,
                bedrooms=1,
                bathrooms=1,
                max_guests=2,
                address='456 Forest Road',
                city='Aspen',
                country='USA',
                amenities=['Fireplace', 'Hot Tub', 'Parking']
            ),
            Listing.objects.create(
                host=host,
                title='Beachfront Villa',
                description='Private villa with direct beach access',
                property_type='VILLA',
                price_per_night=250.00,
                bedrooms=3,
                bathrooms=2,
                max_guests=6,
                address='789 Ocean Drive',
                city='Miami',
                country='USA',
                amenities=['Pool', 'BBQ Grill', 'Beach Access']
            )
        ]

        self.stdout.write('Creating sample bookings...')
        today = datetime.now().date()
        for i, listing in enumerate(listings):
            guest = guest1 if i % 2 == 0 else guest2
            start_date = today + timedelta(days=(i+1)*7)
            end_date = start_date + timedelta(days=random.randint(2, 7))
            
            Booking.objects.create(
                listing=listing,
                guest=guest,
                start_date=start_date,
                end_date=end_date,
                status='CONFIRMED' if i % 2 == 0 else 'PENDING'
            )

        self.stdout.write('Creating sample reviews...')
        for listing in listings:
            Review.objects.create(
                listing=listing,
                guest=guest1,
                rating=random.randint(4, 5),
                comment=f"Great place! {random.choice(['Would definitely stay again.', 'Perfect location.', 'Highly recommended.'])}"
            )
            Review.objects.create(
                listing=listing,
                guest=guest2,
                rating=random.randint(3, 5),
                comment=f"Nice stay. {random.choice(['Could use some improvements.', 'Enjoyed our time here.', 'Good value for money.'])}"
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))