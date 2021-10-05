from .views import HomePageView, LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
