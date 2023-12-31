from rest_framework import serializers
from home.models import Contact,Details,Experts,HomeDetails

class HomeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= HomeDetails
        fields=(
            'main_banner',
            'main_banner_url',
            'sub_banner',
            'sub_banner_url',
            'project_logo',
        )



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=(
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
        )

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields=(
            'heading',
            'body',
            'image',
            'title',
            'content',
        )


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experts
        fields=(
            'title',
            'content',
            'name',
            'role', 
            'experience',
            'photo',
            'rating',
            'counselling',
        )