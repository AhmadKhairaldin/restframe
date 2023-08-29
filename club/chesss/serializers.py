from rest_framework import serializers
from .models import match,club,player,member,tournament

class playerSerializers(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = '__all__'

class memberSerializers(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'

class tournamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = tournament
        fields = '__all__'


class clubSerializers(serializers.ModelSerializer):
    class Meta:
        model = club
        fields = '__all__'

class matchSerializers(serializers.ModelSerializer):
    class Meta:
        model = match
        fields = '__all__'
