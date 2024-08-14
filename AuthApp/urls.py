from django.urls import path
from AuthApp.views import LoginView, LoggedInUsersView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', LoggedInUsersView.as_view(), name='logged_in_users'),
]
