from rest_framework import serializers
from services.models import ServiceType,CourseType

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceType
        fields=(
            'service',
        )

        
class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseType
        fields=(
            'course_type',
        )
        