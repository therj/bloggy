from .views import SignUpView
from django.urls import path
# accounts/urls.py
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
