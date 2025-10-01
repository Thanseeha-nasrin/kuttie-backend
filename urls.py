from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.tasks_list),
    path('leaderboard/', views.leaderboard),
    path('submit/', views.submit_task),
]
