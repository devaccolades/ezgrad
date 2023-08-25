from django.contrib import admin
from question.models import Questions,Options, RecordAnswer

class QuestionsAdmin(admin.ModelAdmin):
    list_display=[
        'question',
    ]
admin.site.register(Questions,QuestionsAdmin)

class OptionsAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'options',
    ]
admin.site.register(Options,OptionsAdmin)

class RecordAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'userid','option']
admin.site.register(RecordAnswer, RecordAnswerAdmin)

# Register your models here.
