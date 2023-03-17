from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    # we need to overwrite the create function
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    