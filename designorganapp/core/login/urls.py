from django.urls import path
from .views import LoginFormView, LogoutView, ResetPasswordView, ChangePasswordView


app_name = 'access'

urlpatterns = [
    # category
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/password/', ResetPasswordView.as_view(), name='reset-password'),
    path('change/password/<str:token>/', ChangePasswordView.as_view(), name='change-password')
]