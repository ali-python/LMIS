from .views import HomePageView, LoginView, LogoutView, UserListView, RegisterView
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('list/user/', UserListView.as_view(), name='user_list'),
    path('user/registration/form/', RegisterView.as_view(), name='register'),
]
