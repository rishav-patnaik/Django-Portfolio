from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('messages/', views.manage_messages, name='manage_messages'),
    path('messages/delete/<int:pk>/', views.delete_message, name='delete_message'),

    path('skill/add/', views.add_skill, name='add_skill'),
    path('skills/manage/', views.manage_skills, name='manage_skills'),
    path('skills/edit/<int:pk>/', views.edit_skill, name='edit_skill'),
    path('skills/delete/<int:pk>/', views.delete_skill, name='delete_skill'),

    path('certification/add/', views.add_certification, name='add_certification'),
    path('certifications/manage/', views.manage_certifications, name='manage_certifications'),
    path('certifications/edit/<int:pk>/', views.edit_certification, name='edit_certification'),
    path('certifications/delete/<int:pk>/', views.delete_certification, name='delete_certification'),

    path('milestone/add/', views.add_milestone, name='add_milestone'),
    path('milestones/manage/', views.manage_milestones, name='manage_milestones'),
    path('milestones/edit/<int:pk>/', views.edit_milestone, name='edit_milestone'),
    path('milestones/delete/<int:pk>/', views.delete_milestone, name='delete_milestone'),



]
