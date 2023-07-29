from rest_framework import serializers
from course.models import University,Facts,Approval,Course

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields=(
         
            'coursetype',
            'university_logo',
            'university_name',
            'about_university',
            'sample_certificate',
            'prospectus',
            'country',

        )

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facts
        fields=(
            'facts',
        )

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Approval
        fields=(
            'approved_by',
            'logo',
        )

class CourseSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields=(
            'course_name',
            'icon',
            'duration',
            'duration_description',
            'course_image',
            'course_details',
            'video',
            'audio',
            'eligibility',
            'eligibility_description',
            'admission_procedure',
            'fees',
            'fees_description',
            'syllabus',
            'country',
            
        )
    def get_country(self, instance):
        if instance.university:
            return instance.university.country
        else:
            return None