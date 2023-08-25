from django.contrib import admin
from home.models import HomeDetails,Contact,Details,Experts,Subbanner
class HomeDetailsAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'main_banner',
        'main_banner_url',
        
    ]
admin.site.register(HomeDetails,HomeDetailsAdmin)


class SubbannerAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'sub_banner',
        'sub_banner_url',
    ]
admin.site.register(Subbanner,SubbannerAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=[
        'id',
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
        'id',
        'heading',
        'body',
        'image',
        'title',
        'content',
        
    ]
admin.site.register(Details,DetailsAdmin)


class ExpertsAdmin(admin.ModelAdmin):
    list_display=[
        'id',
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

