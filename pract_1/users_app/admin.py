from django.contrib import admin
from .models import User, Profile

# Реєструємо твою кастомну модель User
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')

# Реєструємо модель Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')