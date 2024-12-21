from rest_framework import serializers
from .models import CustomUser  # Ensure this is correctly imported

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['pseudo', 'firstname', 'lastname', 'téléphone', 'email', 'password']

    def create(self, validated_data):
        customUser = CustomUser(
            pseudo=validated_data['pseudo'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            téléphone=validated_data['téléphone'],
            email=validated_data['email'],
        )
        customUser.set_password(validated_data['password'])  # Hash the password
        customUser.save()
        return customUser
