# ALX Travel App

A comprehensive vacation rental platform with property listings, booking system, and review functionality.

## Features

- **Property Listings**: 
  - Multiple property types (apartments, houses, villas, cabins)
  - Detailed descriptions with amenities
  - Location-based searching

- **Booking System**:
  - Date-based availability
  - Automatic price calculation
  - Multiple booking statuses (Pending/Confirmed/Completed)

- **Review System**:
  - 1-5 star ratings
  - Guest comments
  - Average rating calculations

- **User Management**:
  - Host/Guest roles
  - Authentication-ready models
  - User profile associations

## Technical Implementation

### Database Models
- **Listing**: Properties available for rent
- **Booking**: Reservation records
- **Review**: Guest feedback system

### API Ready
- RESTful serializers for all models
- Relationship handling (users-listings-bookings)
- Read-only fields for calculated values

### Development Utilities
- Seeder command (`python manage.py seed`)
  - Creates sample users (1 host, 2 guests)
  - Generates 3 property listings
  - Populates with bookings and reviews
- UUID primary keys
- Automatic timestamps (created/updated)

## Setup

1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Seed database: `python manage.py seed`
5. Start server: `python manage.py runserver`

## Technology Stack

- Django (Python)
- Django REST Framework
- PostgreSQL (or SQLite for development)
- UUID for object identification
- JSONField for flexible amenities storage