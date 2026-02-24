from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    # Вкладений серіалізатор: коли ми запитуємо юзера, 
    # ми одразу отримаємо список усіх його профілів
    profiles = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'created_at', 'profiles']
        # Робимо пароль write_only, щоб він ніколи не повертався у відповіді API
        extra_kwargs = {'password': {'write_only': True}}