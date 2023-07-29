from rest_framework import serializers
from course.models import University,Facts,Approval,Course,Country

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
    university = serializers.SerializerMethodField()
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
            'university',
            
        )
    # def get_country(self, instance):
    #     if instance.university:
    #         return instance.university.country
    #     else:
    #         return None
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

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=(
            'country',
            'flag',
        )