import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit.models import User, FitnessActivity
from django.db import IntegrityError

# Clear existing data
User.objects.all().delete()
FitnessActivity.objects.all().delete()

# Add test data with error handling
try:
    users = [
        User(username='john_doe', email='john@example.com'),
        User(username='jane_doe', email='jane@example.com'),
        User(username='alice_smith', email='alice@example.com'),
        User(username='bob_brown', email='bob@example.com')
    ]
    User.objects.bulk_create(users)

    activities = [
        FitnessActivity(user=users[0], activity_type='Running', duration_minutes=30),
        FitnessActivity(user=users[1], activity_type='Cycling', duration_minutes=45),
        FitnessActivity(user=users[2], activity_type='Swimming', duration_minutes=60),
        FitnessActivity(user=users[3], activity_type='Yoga', duration_minutes=50)
    ]
    FitnessActivity.objects.bulk_create(activities)

    print("Test data added successfully!")
except IntegrityError as e:
    print(f"Error adding test data: {e}")
