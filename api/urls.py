from django.contrib import admin              # ← Add this
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, LeaderboardViewSet, SubmissionViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'submissions', SubmissionViewSet, basename='submission')

urlpatterns = [
    path('admin/', admin.site.urls),         # ← Now admin is defined
    path('api/', include(router.urls)),
]

