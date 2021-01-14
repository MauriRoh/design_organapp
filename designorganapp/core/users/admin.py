from django.contrib import admin
from .models import User

# USER
class ModelAdminUsers(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'password',
        'date_joined',
        'last_login',
        'email',
        'gender',
        'image',
        'is_superuser',
        'is_staff',
        'is_active',
        'token',
    )

# Register your models here.
admin.site.register(User, ModelAdminUsers)
