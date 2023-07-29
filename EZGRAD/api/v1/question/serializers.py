from rest_framework import serializers
from question.models import Questions,Options,RecordAnswer

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields=(
            'question',
        )
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Options
        fields=(
            'options',
        )

class RecordAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecordAnswer
        fields=(
            'option',
            'userid'
        )



   

    
        
    
