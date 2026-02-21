from django.urls import path
from .views import (
    ProjectListAPI,
    ProjectDetailAPI,
    ProjectCreateAPI,
    ContactCreateAPI,
)

urlpatterns = [
    path('projects/', ProjectListAPI.as_view()),
    path('projects/<slug:slug>/', ProjectDetailAPI.as_view()),
    path('projects/create/', ProjectCreateAPI.as_view()),
    path('contact/', ContactCreateAPI.as_view()),
]