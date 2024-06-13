
from django.urls import path 
from .views import RegisterUserView , CustomLoginView

app_name='account'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # Add other app-specific URLs here if needed
]