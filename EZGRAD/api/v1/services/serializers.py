from rest_framework import serializers
from services.models import ServiceType,CourseType

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceType
        fields=(
            'id',
            'service',
        )

        
class CourseTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CourseType
        fields=(
            'id',
            'course_type',
        )
    def to_representation(self, obj):
      return {"id":obj.id,"value":obj.course_type}        