from rest_framework import serializers
from question.models import Questions,Options,RecordAnswer

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields=(
            'question',
        )
class OptionSerializer(serializers.ModelSerializer):
    # question = serializers.SerializerMethodField()
    class Meta:
        model=Options
        fields=(
            'options',
            # 'question',
        )
    # def get_question(self, instance):
    #     if instance.question:
    #         return instance.question.question
    #     else:
    #         return None

class RecordAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecordAnswer
        fields=(
            'option',
            'userid'
        )



   

    
        
    
