from django.contrib import admin
from question.models import Questions,Options

class QuestionsAdmin(admin.ModelAdmin):
    list_display=[
        'question',
    ]
admin.site.register(Questions,QuestionsAdmin)

class OptionsAdmin(admin.ModelAdmin):
    list_display=[
        'options',
    ]
admin.site.register(Options,OptionsAdmin)

# Register your models here.
