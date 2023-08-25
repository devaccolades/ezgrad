from rest_framework import serializers
from course.models import University,Facts,Approval,Course,Country,CourseSpecialization,Faq,FoodFacility,Hostel

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
    university=serializers.SerializerMethodField()
    class Meta:
        model=Facts
        fields=(
            'university',
            'id',
            'facts',
           
        )
    def get_university(self,instance):
        if instance.university:
            return instance.university.university_name
        else:
            return None

class ApprovalSerializer(serializers.ModelSerializer):
    university=serializers.SerializerMethodField()
    class Meta:
        model=Approval
        fields=(
            'university',
            'approved_by',
            'logo',
        )
    def get_university(self,instance):
        if instance.university:
            return instance.university.university_name
        else:
            return None

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
    course=serializers.SerializerMethodField()
    class Meta:
        model=CourseSpecialization
        fields=(
            'course',
            'specialization',
            
        )
    def get_course(self,instance):
        if instance.course:
            return instance.course.course_name
        else:
            return None

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

class FoodFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodFacility
        fields=(
            'university',
            'name',
            'photo',
            'fees',
        )

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hostel
        fields=(
            'university',
            'hostel_name',
            'hostel_image',
            'distance',
            'fees',
        )