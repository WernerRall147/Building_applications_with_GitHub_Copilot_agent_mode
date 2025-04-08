import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit.models import User, FitnessActivity

# Add test data
users = [
    User(username='john_doe', email='john@example.com'),
    User(username='jane_doe', email='jane@example.com')
]
User.objects.bulk_create(users)

activities = [
    FitnessActivity(user=users[0], activity_type='Running', duration_minutes=30),
    FitnessActivity(user=users[1], activity_type='Cycling', duration_minutes=45)
]
FitnessActivity.objects.bulk_create(activities)

print("Test data added successfully!")
