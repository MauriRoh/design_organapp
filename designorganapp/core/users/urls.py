from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserChangeGroup, UserProfileView, UserChangePasswordView

app_name = 'user'

urlpatterns = [
    # USER
    path('list/', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('change/group/<int:pk>/', UserChangeGroup.as_view(), name='user-change-group'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('change/password/', UserChangePasswordView.as_view(), name='user-change-password'),
]
