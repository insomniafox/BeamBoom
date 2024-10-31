from rest_framework import serializers

from apps.users.models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'bio',
            'avatar'
        )
        read_only_fields = (
            'avatar',
        )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'created_at',
            'updated_at',
            'profile'
        )
