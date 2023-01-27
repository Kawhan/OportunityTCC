from django.urls import path
from auth_django.views import RegisterView, ChangePasswordView, VerifyEmail, loginAPIView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', loginAPIView.as_view(), name='login_view'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('email_verify', VerifyEmail.as_view(), name='email_verify'),
]
