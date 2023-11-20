from rest_framework import serializers
from actors.models import *


class ActorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
