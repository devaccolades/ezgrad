from rest_framework import serializers
from general.models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=(
            
            'name',
            'email',
            'mobile',
            'gender',
            'dob',
            'country',
        )

class AddregisterSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.CharField()
    mobile=serializers.IntegerField()
    gender=serializers.CharField()
    dob=serializers.DateField()
    country=serializers.CharField()

