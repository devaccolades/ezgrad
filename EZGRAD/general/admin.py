from django.contrib import admin
from general.models import ChiefProfile

class ChiefProfileAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'username',
        'password',
        'confirm_password',
    ]
admin.site.register(ChiefProfile,ChiefProfileAdmin)

# Register your models here.
