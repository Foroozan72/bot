# auth/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'phone')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True, 'validators': [UniqueValidator(queryset=User.objects.all())]},
            'phone': {'required': True, 'validators': [UniqueValidator(queryset=User.objects.all())]},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Accepts either email or phone along with password.
    """

    email_or_phone = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        email_or_phone = data.get('email_or_phone')
        password = data.get('password')

        # Check if the input is an email or phone
        try:
            user = User.objects.get(email=email_or_phone)
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone=email_or_phone)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid credentials.')

        # Authenticate the user
        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError('Login failed.')

        data['user'] = user
        return data