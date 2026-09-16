from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:id>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:id>/delete/', views.delete_student, name='delete_student'),
]