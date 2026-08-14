from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, MeView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginView.as_view(), name=''),
    path('me/', MeView.as_view(), name='me')
]


