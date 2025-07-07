from django.urls import path
from .views import RegisterView, LoginView
from typing import List

urlpatterns: List[path] = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
] 