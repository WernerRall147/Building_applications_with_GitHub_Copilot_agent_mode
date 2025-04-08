from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import api_root

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboards', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

urlpatterns = [
    path('api/', include(router.urls)),  # Move router URLs under 'api/'
    path('', api_root, name='api-root'),  # Map root URL to api_root
]
