from rest_framework import serializers
from general.models import StudentProfile,ReviewStudent

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfile
        fields=(
            'name',
            'email',
            'mobile',
            'gender',
            'dob',
        )

class AddStudentProfileSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.CharField()
    mobile=serializers.IntegerField()
    gender=serializers.CharField()
    dob=serializers.DateField()
    
class ChiefProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    mobile = serializers.IntegerField()

class ReviewStudentSerializer(serializers.Serializer):
    class Meta:
        model=ReviewStudent
        fields=(
            'name',
            'rating',
            'review',

    )

