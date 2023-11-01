from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateAccountApiView, VerifyAccountApiView

urlpatterns = [
    path('create', CreateAccountApiView.as_view(), name='create_account'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('verify/<token>', VerifyAccountApiView.as_view(), name='verify')
]
