from rest_framework import serializers
from .models import User
from rest_framework import exceptions

class UserCreationSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password','re_password']

        extra_kwargs = {
            'password' : {
                'write_only' : True
            },
        }

    def validate(self, attrs):
        if not attrs['re_password'] == attrs['password']:
            raise exceptions.NotAcceptable()
        attrs.pop('re_password')
        return super().validate(attrs)
        

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.is_active = False
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']