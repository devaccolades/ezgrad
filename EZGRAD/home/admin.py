from django.contrib import admin
from home.models import HomeDetails,Contact,Details,Experts
class HomeDetailsAdmin(admin.ModelAdmin):
    list_display=[
        'main_banner',
        'main_banner_url',
        'sub_banner',
        'sub_banner_url',
        'project_logo',
        
    ]
admin.site.register(HomeDetails,HomeDetailsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=[
        'logo',
        'about',
        'address',
        'phone',
        'email',
        'facebook_url',
        'instagram_url',
        'youtube_url',
        'whatsapp_url',
        'linkedln_url',
    ]
admin.site.register(Contact,ContactAdmin)



class DetailsAdmin(admin.ModelAdmin):
    list_display=[
        'heading',
        'body',
        'image',
        'title',
        'content',
        
    ]
admin.site.register(Details,DetailsAdmin)


class ExpertsAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'content',
        'name',
        'role',
        'experience',
        'photo',
        'rating',
        'counselling',
       
    ]
admin.site.register(Experts,ExpertsAdmin)


# Register your models here.

