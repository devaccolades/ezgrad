from rest_framework import serializers
from question.models import Questions,Options,RecordAnswer

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields=(
            'question',
        )
class OptionSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    class Meta:
        model=Options
        fields=(
            'options',
            'question',
        )
    def to_representation(self, obj):
      return  obj.options
    def get_question(self, instance):
        if instance.question:
            return instance.question.question
        else:
            return None

class RecordAnswerSerializer(serializers.ModelSerializer):
    question=serializers.SerializerMethodField()
    userid=serializers.SerializerMethodField()
    class Meta:
        model=RecordAnswer
        fields=(
            'id',
            'userid',
            'question',
            'option',
           
        )
    def get_question(self,instance):
        if instance.option.question:
            return instance.option.question.question
        else:
            return None
    def get_userid(self,instance):
        if instance.userid:
            return instance.userid.name
        else:
            return None
   



   

    
        
    
