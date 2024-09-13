from django.urls import path
from .views import RegisterPageView, HomePageVew

urlpatterns = [
    path('', HomePageVew.as_view(), name='home'),
    path('register/', RegisterPageView.as_view(), name='register'),
]