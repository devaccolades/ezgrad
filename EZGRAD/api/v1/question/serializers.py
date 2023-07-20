from rest_framework import serializers
from question.models import Questions,Options

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



   

    
        
    
