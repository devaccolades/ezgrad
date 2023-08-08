from rest_framework import serializers
from course.models import University,Facts,Approval,Course,Country,CourseSpecialization,Faq

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

class CourseviewSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields=(
            'course_name',
            'icon',
            'duration',
            'university',
            
        )

    def get_university(self,instance):
        request = self.context["request"]
        if instance.university:
            selected_categories = instance.university.country.all()

            serialized_data = CountrySerializer(
                selected_categories,
                context = {
                    "request" : request
                },
                many=True
            ).data

            return serialized_data
        else:
            return None

class CourseSerializer(serializers.ModelSerializer):
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
            
        )
class CourseSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseSpecialization
        fields=(
            'specialization',
        )

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=(
            'country',
            'flag',
        )

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq
        fields=(
            'faq_question',
            'faq_answer',
        )