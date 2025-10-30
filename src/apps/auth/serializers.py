from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Esse email já está cadastrado")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['username'] = validated_data['email']
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class PasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class PasswordResetConfirmSerializer(serializers.ModelSerializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['uid', 'token', 'new_password']