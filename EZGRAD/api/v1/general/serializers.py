from rest_framework import serializers
from general.models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields=(
            
            'name',
            'email',
            'mobile',
            'gender',
            'dob',
            'country',
        )

class AddStudentProfileSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.CharField()
    mobile=serializers.IntegerField()
    gender=serializers.CharField()
    dob=serializers.DateField()
    country=serializers.CharField()

class ChiefProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    mobile = serializers.IntegerField()