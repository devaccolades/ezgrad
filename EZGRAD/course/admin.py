from django.contrib import admin
from course.models import University,Facts,Approval,Course,CourseSpecialization,Country,Faq,FoodFacility,Hostel

class UniversityAdmin(admin.ModelAdmin):
    list_display=[
       'id',
       'coursetype',
       'university_logo',
       'university_name',
       'about_university',
       'sample_certificate',
       'prospectus',
       'get_country',
    ]
    def get_country(self, obj):
        return "\n".join([c.country for c in obj.Country.all()])
admin.site.register(University,UniversityAdmin)

class FactAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'university',
        'facts',
    ]
admin.site.register(Facts,FactAdmin)

class ApprovalAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'university',
        'approved_by',
        'logo',
    ]
admin.site.register(Approval,ApprovalAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'university',
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
    ]
admin.site.register(Course,CourseAdmin)

class CourseSpecializationAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'course',
        'specialization',
    ]
admin.site.register(CourseSpecialization,CourseSpecializationAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'country',
        'flag',
    ]
admin.site.register(Country,CountryAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'course',
        'faq_question',
        'faq_answer',
    ]
admin.site.register(Faq,FaqAdmin)

class FoodFacilityAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'university',
        'name',
        'photo',
        'fees',
    ]
admin.site.register(FoodFacility,FoodFacilityAdmin)


class HostelAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'hostel_name',
        'hostel_image',
        'distance',
        'fees',
    ]
admin.site.register(Hostel,HostelAdmin)
# Register your models here.
