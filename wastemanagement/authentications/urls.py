# urls.py

from django.urls import path
from .views import SignUpView, SignInView, UserDetailView,UserListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='api_signup'),
    path('signin/', SignInView.as_view(), name='api_signin'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='api_user_detail'),
 path('users/', UserListView.as_view(), name='api_user_list'),

]
