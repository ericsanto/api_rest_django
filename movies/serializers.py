from rest_framework import serializers
from movies.models import Movie


class MovieSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                'Resumo excedeu o limite máximo de caractere. Limite máximo: 200 caracteres')
        return value

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                'O título do filme, deve ter, pelo menos, 3 caracteres')
        return value
