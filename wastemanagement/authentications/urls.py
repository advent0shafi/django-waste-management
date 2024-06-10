# urls.py

from django.urls import path
from .views import SignUpView, SignInView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='api_signup'),
    path('signin/', SignInView.as_view(), name='api_signin'),
]
