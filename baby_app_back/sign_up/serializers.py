from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only':True} #to hide the password
        }

    def save(self):
        user = User.objects.create (
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        
        if password != confirm_password:
            raise serializers.ValidationError({'password ': 'password does not match'})
        user.set_password(password)
        user.save()
        return user