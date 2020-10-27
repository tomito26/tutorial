from rest_framework import serializers
from .models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('title','description','image','content','author','published','created_on','updated_on')