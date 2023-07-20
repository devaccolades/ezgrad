from django.contrib import admin
from services.models import ServiceType
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display=[
        'service',
    ]
admin.site.register(ServiceType,ServiceTypeAdmin)
# Register your models here.
