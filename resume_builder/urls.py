

from django.urls import path
from builder import views

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('display_resume/', views.display_resume, name='resume_display'),
    # Add more URLs as needed
]
